import json
import requests
from jira import JIRA


class JiraData:
    """
    A class used to extract issues from bmw-cc jira.
    ...
    Attributes
    ----------
    token : str
        a string used for token-based authentication
    jira_base_url : str
        jira url
    query_issue : str
        query used to retrieve issues
    jira_connector : jira instance
        the jira connector
    Methods
    -------
    connect_to_jira()
        Connect to jira server
    extract_jira_issues(query)
        Retrieve jira issues from a given query
    extract_jira_issues(query)
        Retrieve jira issues from a given query
    get_all_fields(project_key, issue_type_name)
        Retrieve all fields of a specific project and also the mapping list between the field id and the actual field
        name
    """

    def __init__(self, token, jira_url):
        """
        Parameters
        ----------
        token : str
            a string used for token-based authentication
        jira_base_url : str
            jira url
        """
        self.token = token
        self.jira_base_url = jira_url
        self.jira_connector = None
        self.query_issue = None
        self.session = None

    def connect_to_jira(self):
        """Connect to jira server."""
        try:
            print("Trying to connect to the jira server...")
            connector = JIRA(
                token_auth=self.token,
                server=self.jira_base_url,
                options={"verify": False},
            )
        except Exception as e:
            print("unable to connect to jira server\n", "Error : " + str(e))
        self.jira_connector = connector

    def make_request_session(self):
        s = requests.Session()
        s.verify = False
        s.headers = {"Authorization": f"Bearer {self.token}"}
        self.session = s

    def extract_jira_issues(self, jql_query, expand=None):
        """Retrieve jira issues from a given query.

        Parameters
        ----------
        jql_query : str
            jql_queries_with_args
        expand : str
            optional arg to pass to jira search_issues
        Returns
        -------
        list
            a list of issues.
        """
        self.query_issue = jql_query["text"].format(*jql_query["arguments"])
        issues = list()
        block_size = 500
        start_idx = 0
        print("Extracting Jira Issues...")
        while True:
            issue_ids = self.jira_connector.search_issues(
                self.query_issue,
                startAt=start_idx,
                maxResults=block_size,
                fields=None,
                expand=expand,
            )

            issues.extend(issue_ids)
            start_idx += block_size
            if len(issue_ids) == 0:
                # Retrieve issues until there are no more to come
                break
        return issues

    def get_issues_commits(self, issue_key):
        """Retrieve commits form the issue key
        Parameters
        ----------
        issue_key : str
            The issue key

        Returns
        -------
        issue_commits : dict
            Dict of commit of issue.
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        url_get = f"{self.jira_base_url}rest/gitplugin/1.0/issues/{issue_key}/commits?showFiles=true"
        issue_response = requests.get(url_get, headers=headers, verify=False)
        issue_commits = issue_response.json()
        return issue_commits

    def extract_issues_reporters(self, projects_names, group_name, field):
        """Retrieve jira issues from a given query.

        Parameters
        ----------
        projects_names : str
            The names of projects to be treated.

        Returns
        -------
        list
            a list of issues.
        """
        projects_names = ",".join(projects_names)
        self.query_issue = (f'project in ({projects_names}) and {field} in membersOf("{group_name}")')
        issues = list()
        block_size = 500
        start_idx = 0
        while True:
            issue_ids = self.jira_connector.search_issues(
                self.query_issue,
                startAt=start_idx,
                maxResults=block_size,
                fields=field,
            )
            issues.extend(issue_ids)
            start_idx += block_size
            if len(issue_ids) == 0:
                # Retrieve issues until there are no more to come
                break
        return issues

    def get_issues_keys(self, project_name, json_result, jql_filter_str=None):
        """Retrieve all jira issues keys of a project.

        Parameters
        ----------
        project_name : str
            The name of project to be treated.

        Returns
        -------
        list
            a list of issues keys.
            :param jql_filter_str:
        """
        query_issue = f'project = "{project_name}"' + (
            jql_filter_str if jql_filter_str else ""
        )
        issues_keys = list()
        block_size = 1000
        start_idx = 0
        has_more_issues = True
        print("Extracting Jira Issues...")
        while has_more_issues:
            issues = self.jira_connector.search_issues(
                query_issue, startAt=start_idx, maxResults=block_size, fields=["key"], json_result=json_result
            )
            has_more_issues = bool(issues["issues"])
            issues_keys.extend([issue["key"] for issue in issues["issues"]])
            start_idx += block_size
        return issues_keys

    def get_all_fields(self, project_key, issue_type_name):
        """Retrieve all fields of a specific project and also the mapping list between the field id and the actual
        field name"""
        # Authenticate using API token
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        # Get the project's configuration
        project_config_response = requests.get(
            f"{self.jira_base_url}rest/api/2/project/{project_key}",
            headers=headers,
            verify=False,
        )
        project_config = project_config_response.json()

        total_fields = []
        matching_list = []
        for issue_type1 in issue_type_name:
            # Get the issue type's ID
            issue_type_id = None
            for issue_type in project_config["issueTypes"]:
                if issue_type["name"] == issue_type1:
                    issue_type_id = issue_type["id"]
                    break

            # If issue type ID found, get the fields associated with it
            if issue_type_id:
                issue_type_config_response = requests.get(
                    f"{self.jira_base_url}rest/api/2/issue/createmeta"
                    f"/{project_key}/issuetypes/{issue_type_id}",
                    headers=headers,
                    verify=False,
                )
                issue_type_fields = issue_type_config_response.json()

                # Print the field names
                for field in issue_type_fields["values"]:
                    if field["fieldId"] not in total_fields:
                        total_fields.append(field["fieldId"])
                        matching_list.append({field["fieldId"]: field["name"]})
            else:
                print(f"Issue type '{issue_type_name}' not found.")
        return total_fields, matching_list

    @staticmethod
    def retrieve_worklogs(issue):
        """
        Extract the worklogs from the issue.
        """
        list_of_dicts = issue.raw["fields"]["worklog"]["worklogs"]
        for d in list_of_dicts:
            d["url"] = d.pop("self")
            d["issue_id"] = issue.key
            d["author"] = d["author"]["name"]
            d["updateAuthor"] = d["updateAuthor"]["name"]
            d["created"] = d["created"][:19]
            d["updated"] = d["updated"][:19]
            d["started"] = d["started"][:19]

        return list_of_dicts

    @staticmethod
    def retrieve_to_do_list(issue):
        """
        Extract the todo field from issue
        """
        res = issue.raw["fields"]["customfield_15101"]
        if res == None:
            return []
        else:
            parsed_list = json.loads(res)
            for d in parsed_list:
                d["issue_id"] = issue.key
            return parsed_list

    def retrieve_boards(self, project):
        return [
            board.id for board in self.jira_connector.boards(projectKeyOrID=project)
        ]

    def retrieve_sprints_from_board(self, board_id):
        try:
            return self.jira_connector.sprints(board_id, maxResults=0)
        except:
            return []

    def retrieve_sprints_from_boards(self, boards_id):
        sprints = [self.retrieve_sprints_from_board(board_id) for board_id in boards_id]
        return sum(sprints, [])

    @staticmethod
    def extract_sprint_data(sprints):
        def handle_missing_keys(sprint):
            sprint["goal"] = sprint.get("goal", None)
            sprint["completeDate"] = sprint.get("completeDate", None)
            sprint["activatedDate"] = sprint.get("activatedDate", None)
            sprint["startDate"] = sprint.get("startDate", None)
            sprint["endDate"] = sprint.get("endDate", None)
            return sprint

        sprints_data = {
            sprint.raw["id"]: handle_missing_keys(sprint.raw) for sprint in sprints
        }
        sprints_data = list(sprints_data.values())
        return sprints_data

    def get_all_users(self, include_inactive=True):
        request_url = (
                self.jira_base_url
                + "rest/api/2/user/search?username=."
                + ("&includeInactive=true" if include_inactive else "")
        )
        users_data = []
        r = self.session.get(request_url + "&maxResults=1000&startAt=0")
        start_at_coef = 1
        while len(r.json()) > 0:
            users_data.extend(r.json())
            r = self.session.get(
                request_url + f"&maxResults=1000&startAt={start_at_coef * 1000}"
            )
            start_at_coef += 1
        return users_data

    def get_server_time(self):
        return self.jira_connector.server_info()["serverTime"]
