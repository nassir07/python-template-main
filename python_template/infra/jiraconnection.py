"""Implement a class used to communicate with jira api."""

import logging

from jira import JIRA

logger = logging.getLogger(__name__)


class JiraConnection:
    """Implement a class used to communicate with jira api."""

    def __init__(self, jira_server, jira_token, options):
        """Initiate the class instance."""
        self.jira_server = jira_server
        self.jira_token = jira_token
        self.options = options

    def connect_to_jira(self) -> bool:
        """Return the Jira instance."""
        self.jira = JIRA(server=self.jira_server, token_auth=self.jira_token, options=self.options)
        return True

    def create_issue(self, fields):
        """Create a Jira issue."""
        return self.jira.create_issue(fields=fields, prefetch=True)

    def create_issues(self, field_list):
        """Create a list of Jira issues."""
        return self.jira.create_issues(field_list=field_list, prefetch=True)

    def search_issues(self, jql_l, selected_fields):
        """Search for Jira issues using a jql."""
        return self.jira.search_issues(jql_l, startAt=0, maxResults=None, fields=selected_fields, expand="names")

    @staticmethod
    def get_issue_fields(issue, fields_map):
        """Get issue fields."""

        def deep_get(value, path_and_type):
            if not path_and_type or value is None:
                return value
            type, path = path_and_type[0]
            if type == "list":
                return [deep_get(ele.get(path), path_and_type[1:]) for ele in value]
            else:
                return deep_get(value.get(path), path_and_type[1:])

        return {result_field: deep_get(issue.raw, path_and_type) for result_field, path_and_type in fields_map.items()}

    def search_issues_fields(self, jql_l, selected_fields, fields_map):
        """Search for Jira issues using a jql and ammping of fileds names."""
        issues = self.search_issues(jql_l, selected_fields)
        return [JiraConnection.get_issue_fields(issue, fields_map) for issue in issues]
