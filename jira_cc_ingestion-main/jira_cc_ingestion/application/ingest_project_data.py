import datetime

from jira_cc_ingestion.application.get_from_db import get_extraction_depth, get_last_row
from jira_cc_ingestion.application.extract_from_jira import (
    retrieve_raw_issues,
    process_issues,
    retrieve_deleted_issue_keys,
    get_sprints_data,
    get_todo_deleted_list,
    get_worklog_deleted_list,
    get_users_data,
    retrieve_worklogs,
    retrieve_to_do_list, retrieve_changelogs,
)
from jira_cc_ingestion.application.load_to_db import (
    loading_info,
    tag_deleted,
    delete_insert_sprints_data,
    loading_deleted_todo,
    loading_deleted_worklog,
    delete_insert_users_data, update_changelog_data,
)
from jira_cc_ingestion.infra.jira import JiraData
from jira_cc_ingestion.infra.sql_db import DatabaseHelper
import logging

logger = logging.getLogger(__name__)


def ingest_project_data(token_auth, user_sql, password_sql, project):
    logger.info("connecting to sql server...")
    connection_string = "mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL+Server".format(
        user_sql, password_sql, project['sql_server'], project['port'], project['sql_db'], project['schema']
    )
    data_connector = DatabaseHelper(connection_string=connection_string, schema=project['schema'])
    logger.info("sql server is ready!")

    logger.info("connecting to jira server...")
    jc = JiraData(token=token_auth, jira_url=project["jira_url"])
    jc.connect_to_jira()
    logger.info("jira server is ready!")

    logger.info("getting current date...")
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"current date is {current_datetime}")

    logger.info(f"Retrieving extraction depth for {project['name']} project... ")
    last_date = get_extraction_depth(data_connector, project)
    logger.info(
        f"Retrieving update issues since {last_date} and configured fields for the {project['name']} project..."
    )
    issues_list = retrieve_raw_issues(jc, project, last_date)
    logger.info(f"update issues  and configured fields are extracted.")

    logger.info(f"Extracting of needed fields for the {project['name']} project...")
    extracted_issues = process_issues(jc, project, issues_list, current_datetime)
    logger.info(f"Needed fields Extracted!")

    logger.info(
        f"Retrieving the last update for each issue for {project['name']} project... "
    )
    existent_data = get_last_row(data_connector, project['sql_table_issue'], ['[key]', 'updated'], ['[key]'], 'updated',
                                 ['deleted'])
    logger.info(f"Data retrieved from the database successfully!")

    logger.info("creating sql session...")
    transaction, connection = data_connector.create_session()
    logger.info("sql session is created!")

    logger.info(f"Loading issues for {project['name']} project...")
    loading_info(
        data_connector,
        connection,
        project["sql_table_issue"],
        extracted_issues,
        existent_data,
        ["key", "updated"],
        project["list_date_fields"],
        project.get("date_fields_format"),
        project.get("process_str_columns"),
        project.get("list_float_fields")
    )
    logger.info(f"issues loaded for {project['name']} project...")

    logger.info("Get keys to tag as deleted")
    keys_to_tag = retrieve_deleted_issue_keys(
        jc, project["name"], existent_data["key"].tolist()
    )
    logger.info(f"Tag keys as deleted: {len(keys_to_tag)}")
    tag_deleted(
        data_connector,
        connection,
        keys_to_tag,
        project["sql_table_issue"],
        "key",
        "deleted",
    )
    logger.info("Keys Tag as deleted")

    if project.get("sql_table_sprints"):
        logger.info("Extracting sprints data...")
        sprints_data = get_sprints_data(jc, project["name"])
        logger.info("Load sprints data...")
        delete_insert_sprints_data(
            data_connector, connection, sprints_data, project["sql_table_sprints"]
        )
        logger.info("Sprints data loaded!")

    if project.get("sql_table_worklogs"):
        logger.info(
            f"Extracting of worklogs fields for the {project['name']} project..."
        )
        extracted_worklogs = retrieve_worklogs(jc, project, issues_list)
        logger.info(f"Worklogs fields Extracted!")
        logger.info(f"Tagging deleted worklogs ids in {project['name']} project...")
        df_worklog_list_were_deleted = get_worklog_deleted_list(
            data_connector, project, extracted_issues, extracted_worklogs
        )
        loading_deleted_worklog(
            data_connector,
            connection,
            project,
            df_worklog_list_were_deleted,
            current_datetime,
        )
        logger.info(
            f"Deleted worklogs ids are retrieved and loaded for {project['name']} project..."
        )

        logger.info(
            f"Retrieving the last update for each worklog for {project['name']} project... "
        )
        existent_worklogs = get_last_row(
            data_connector,
            project["sql_table_worklogs"],
            ["issue_id", "id", "updated"],
            ["issue_id", "id"],
            "updated",
            ["worklog_is_deleted", "issue_is_deleted"],
        )
        logger.info(f"Data retrieved from the database successfully!")
        logger.info(f"Loading worklogs for {project['name']} project...")
        loading_info(
            data_connector,
            connection,
            project["sql_table_worklogs"],
            extracted_worklogs,
            existent_worklogs,
            ["issue_id", "id", "updated"],
            project["list_date_fields"],
            project.get("worklogs_date_fields_format"),
            project.get("process_str_columns"),
        )
        logger.info(f"worklogs loaded for {project['name']} project...")
        logger.info(f"Tag keys as deleted: {len(keys_to_tag)}")
        tag_deleted(
            data_connector,
            connection,
            keys_to_tag,
            project["sql_table_worklogs"],
            "issue_id",
            "issue_is_deleted",
        )
        logger.info("Keys Tag as deleted")

    if project.get("sql_table_todo_list"):
        logger.info(f"Extracting of todo fields for the {project['name']} project...")
        extracted_to_do_list = retrieve_to_do_list(issues_list, current_datetime, project)
        logger.info(f"todo fields Extracted!")

        logger.info(f"Tagging deleted todo ids in {project['name']} project...")
        df_todo_list_were_deleted = get_todo_deleted_list(
            data_connector, project, extracted_issues, extracted_to_do_list
        )
        loading_deleted_todo(
            data_connector,
            connection,
            project,
            df_todo_list_were_deleted,
            current_datetime,
        )
        logger.info(
            f"Deleted todo ids are retrieved and loaded for {project['name']} project..."
        )

        logger.info(
            f"Retrieving the last update for the to do list for {project['name']} project... "
        )
        existent_todo = get_last_row(
            data_connector,
            project["sql_table_todo_list"],
            ["issue_id", "id", "type", "mandatory", "status"],
            ["issue_id", "id"],
            "date_of_insert",
            ["todo_is_deleted", "issue_is_deleted"],
        )
        logger.info(f"Data retrieved from the database successfully!")
        logger.info(f"Loading to do list for {project['name']} project...")
        loading_info(
            data_connector,
            connection,
            project["sql_table_todo_list"],
            extracted_to_do_list,
            existent_todo,
            ["issue_id", "id", "type", "mandatory", "status"],
            process_str_columns=project.get("process_str_columns"),
        )
        logger.info(f"to do list loaded for {project['name']} project...")
        logger.info(f"Tag keys as deleted: {len(keys_to_tag)}")
        tag_deleted(
            data_connector,
            connection,
            keys_to_tag,
            project["sql_table_todo_list"],
            "issue_id",
            "issue_is_deleted",
        )
        logger.info("Keys Tag as deleted")

    if project.get("sql_table_changelog"):
        logger.info(f"Extracting of changelog for the {project['name']} project...")
        extracted_changelog = retrieve_changelogs(project, issues_list)
        logger.info(f"changelog  extracted!")
        logger.info(f"Loading changelog for {project['name']} project...")
        update_changelog_data(
            data_connector,
            connection,
            extracted_changelog.to_dict(orient='records'),
            project["sql_table_changelog"],
            project["changelog_schema"]

        )

    if project.get("sql_table_users"):
        logger.info("Extract users data!")
        users_data = get_users_data(jc)
        logger.info("Load users data!")
        delete_insert_users_data(
            data_connector, connection, users_data, project["sql_table_users"]
        )
        logger.info("users data loaded")

    transaction.commit()
