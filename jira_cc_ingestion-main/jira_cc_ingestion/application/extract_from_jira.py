import json
import re

import numpy as np
import pandas as pd

from jira_cc_ingestion.application.get_from_db import (
    get_todo_list_for_updated_issues,
    get_worklog_list_for_updated_issues,
)
from jira_cc_ingestion.application.utils import join_list
from jira_cc_ingestion.infra import jira_issue_extractor


def retrieve_raw_issues(jc, project, list_of_days):
    """connect to the jira server and get issues of all projects"""
    jql_query = {
        "text": 'project = "{}" and updated >= "{}" {}',
        "arguments": [
            project["name"],
            list_of_days,
            project.get("additional_conditions", ""),
        ],
    }
    issues = jc.extract_jira_issues(jql_query, expand=project.get("expand"))
    return issues


def retrieve_reporters_from_groups(jc, groups_map, projects):
    groups_dict = {
        Department: set(
            [
                issue.raw["fields"]["reporter"]["name"]
                for issue in jc.extract_issues_reporters(projects, group, "reporter")
            ]
            + [
                issue.raw["fields"]["assignee"]["name"]
                for issue in jc.extract_issues_reporters(projects, group, "assignee")
            ]
        )
        for group, Department in groups_map.items()
    }
    list_of_tuples = [(key, value) for key, values in groups_dict.items() for value in values]
    return pd.DataFrame(list_of_tuples, columns=["Department", "Reporter"])


def retrieve_reporters(jc, groups, projects, current_datetime):
    groups_dict = {
        group: set(
            [extract_reporter_info(issue) for issue in jc.extract_issues_reporters(projects, group)]
        )
        for group in groups
    }
    list_of_tuples = [
        (key, *tup, current_datetime) for key, values in groups_dict.items() for tup in values
    ]
    reporters_data = pd.DataFrame(
        list_of_tuples,
        columns=["group", "reporter_name", "reporter_display_name", "date_of_insert"],
    )
    return reporters_data


def extract_reporter_info(issue):
    reporter = issue.raw["fields"]["reporter"]
    reporter_name = reporter["name"]
    reporter_display_name = reporter["displayName"]
    return reporter_name, reporter_display_name


def retrieve_deleted_issue_keys(jc, project_name, db_undeleted_issues):
    """connect to the jira server and get issues of all projects"""
    current_issues_keys = jc.get_issues_keys(project_name, json_result=True)
    issues_to_delete = set(db_undeleted_issues) - set(current_issues_keys)
    return issues_to_delete


def process_issues(jc, project_dict, issues_list, current_datetime):
    """processing issues to generate a dataframe contains issues information"""
    extracted_issues = pd.DataFrame(
        [
            extract_fields(jc, project_dict, issue, issue.fields, project_dict["list_of_fields"])
            for issue in issues_list
        ]
    )
    extracted_issues["date_of_insert"] = current_datetime
    extracted_issues["deleted"] = 0
    return extracted_issues


def retrieve_worklogs(jc, project_dict, issues_list):
    worklogs_list = []
    for issue in issues_list:
        if issue.fields.worklog.total <= issue.fields.worklog.maxResults:
            worklogs = issue.fields.worklog.worklogs
        else:
            worklogs = jc.jira_connector.worklogs(issue.key)

        if worklogs:
            worklogs_list.extend(
                [
                    extract_fields(
                        jc, project_dict, issue, worklog, project_dict["list_of_worklog_fields"]
                    )
                    for worklog in worklogs
                ]
            )
    return (
        pd.DataFrame(worklogs_list)
        .rename(columns={"issue_id": "issueId"})
        .rename(columns={"key": "issue_id"})
    )


def retrieve_changelogs(project_dict, issues_list):
    changelog_list = [
        [
            issue.key,
            item.field,
            h.created,
            item.fromString,
            item.toString,
            getattr(h.author, project_dict.get("author_name")),
        ]
        for issue in issues_list
        for h in issue.changelog.histories
        for item in h.items
        if item.field in project_dict.get("changelog_fields", []) and hasattr(h, "author")
    ]
    return pd.DataFrame(
        changelog_list, columns=["key", "field", "change_date", "from_value", "to_value", "author"]
    )


def retrieve_to_do_list(issues_list, current_datetime, project):
    """
    Extract the todo field from issue
    """
    field_to_parse = project.get("to_do_field")
    to_do_list = []
    for issue in issues_list:
        res = issue.raw["fields"][field_to_parse]
        if res:
            input_list = json.loads(res) if isinstance(res, str) else res
            for d in input_list:
                if d.get("todo", None) != "[]":
                    rest_dict = dict()
                    rest_dict["issue_id"] = issue.key
                    rest_dict["status"] = (
                        d.get("status", dict()).get("name", "")
                        if isinstance(d.get("status"), dict)
                        else d.get("status")
                    )
                    rest_dict["id"] = d.get("todo", d.get("id", ""))
                    rest_dict["type"] = d.get("type", "")
                    rest_dict["mandatory"] = d.get("mandatory", "")
                    rest_dict["linkedIssueKey"] = d.get("linkedIssueKey", "")

                    to_do_list.append(rest_dict)
    to_do_df = pd.DataFrame(to_do_list)
    to_do_df["todo_is_deleted"] = 0
    to_do_df["date_of_insert"] = current_datetime
    return to_do_df


def extract_fields(jc, project_dict, issue, fields_dict, list_of_fields):
    """extract fields"""
    list_info = (
        [
            getattr(jira_issue_extractor, field_dict["method_of_extraction"])(
                vars(fields_dict).get(field_dict["corresponding_customfield"]),
                *field_dict.get("arguments", [])
            )
            for field_dict in list_of_fields
        ]
        + [
            getattr(jira_issue_extractor, field_dict["method_of_extraction"])(
                vars(issue).get(field_dict["corresponding_customfield"]),
                *field_dict.get("arguments", [])
            )
            for field_dict in project_dict["list_of_direct_fields"]
        ]
        + [
            getattr(jira_issue_extractor, field_dict["method_of_extraction"])(jc=jc, issue=issue)
            for field_dict in project_dict.get("list_of_fields_with_specific_extraction", [])
        ]
    )

    fields_names = (
        [field_dict["field"] for field_dict in list_of_fields]
        + [field_dict["field"] for field_dict in project_dict["list_of_direct_fields"]]
        + [
            field_dict["field"]
            for field_dict in project_dict.get("list_of_fields_with_specific_extraction", [])
        ]
    )

    return dict(zip(fields_names, list_info))


def get_sprints_data(jc, project):
    boards_id = jc.retrieve_boards(project)
    sprints = jc.retrieve_sprints_from_boards(boards_id)
    sprints_data = jc.extract_sprint_data(sprints)
    return sprints_data


def get_users_data(jc):
    if not jc.session:
        jc.make_request_session()
    users_data = jc.get_all_users()
    users_data = [
        {
            "key": user_data["key"],
            "name": user_data["name"],
            "emailAddress": user_data["emailAddress"],
            "displayName": user_data["displayName"],
            "active": user_data["active"],
            "deleted": user_data["deleted"],
        }
        for user_data in users_data
    ]
    return users_data


def get_todo_deleted_list(data_connector, project, extracted_issues, df_todo_extracted):
    list_updated_issues = list(extracted_issues["key"]) if not extracted_issues.empty else []
    df_todo_list_for_updated_issues = get_todo_list_for_updated_issues(
        data_connector, project, list_updated_issues
    )
    df_todo_extracted["id"] = df_todo_extracted["id"].str.replace("\t", "")
    df_todo_extracted["id"] = df_todo_extracted["id"].str.replace(" ", "")
    df_todo_list_for_updated_issues["id"] = df_todo_list_for_updated_issues["id"].str.replace(
        "\t", ""
    )
    df_todo_list_for_updated_issues["id"] = df_todo_list_for_updated_issues["id"].str.replace(
        " ", ""
    )
    filter_values = pd.DataFrame({"id": df_todo_extracted["id"]})
    filter_values = filter_values.fillna(np.nan).replace([np.nan], [None])
    df = df_todo_list_for_updated_issues[
        ~df_todo_list_for_updated_issues[["id"]].isin(filter_values.to_dict("list")).all(axis=1)
    ][["id", "type", "issue_id", "mandatory", "status"]]
    df["todo_is_deleted"] = 1
    df["issue_is_deleted"] = 0
    return df


def get_worklog_deleted_list(data_connector, project, extracted_issues, df_worklog_extracted):
    list_updated_issues = list(extracted_issues["key"]) if not extracted_issues.empty else []
    df_worklog_list_for_updated_issues = get_worklog_list_for_updated_issues(
        data_connector, project, list_updated_issues
    )
    if not df_worklog_extracted.empty:
        filter_values = pd.DataFrame({"id": df_worklog_extracted["id"]})
    else:
        filter_values = pd.DataFrame()
    filter_values = filter_values.fillna(np.nan).replace([np.nan], [None])
    df = df_worklog_list_for_updated_issues[
        ~df_worklog_list_for_updated_issues[["id"]].isin(filter_values.to_dict("list")).all(axis=1)
    ][
        [
            "id",
            "author",
            "updateAuthor",
            "comment",
            "created",
            "updated",
            "started",
            "timeSpent",
            "issue_id",
            "timeSpentSeconds",
            "issueId",
            "url",
        ]
    ]
    df["worklog_is_deleted"] = 1
    df["issue_is_deleted"] = 0
    return df


def retrieve_filtered_reporters(jira_connector, filter_department_map):
    reporters_list = []

    for filter_id, department in filter_department_map.items():
        filter_details = jira_connector.filter(filter_id)
        filter_jql = filter_details.jql
        match = re.search(r"in\s+\((.*?)\)", filter_jql)

        if match:
            reporter_names = [name.strip() for name in match.group(1).split(",")]
            for name in reporter_names:
                reporters_list.append({"Reporter": name, "Department": department})

    final_dataframe = pd.DataFrame(reporters_list)
    return final_dataframe


def get_commits_from_issues(commits_list, issues):
    """Create a pandas dataframe contains commits of issues
    input :
        commits_list : list
            commits information
        issues : list
            issues list

    output :
        df_commits : pd.dataframe
    """
    df_commits = pd.DataFrame(
        columns=["ticket", "commitId", "isMergeCommit", "date", "message", "branches"]
    )
    for i, issue in enumerate(issues):
        if commits_list[i]:
            df = pd.DataFrame(commits_list[i])[
                ["commitId", "isMergeCommit", "date", "message", "branches"]
            ]
            df["ticket"] = issue.key
            df_commits = pd.concat([df_commits, df], ignore_index=True)
    df_commits["branches"] = df_commits["branches"].apply(join_list)
    return df_commits
