import os

# Sql server
SQL_SERVER = "testtooldata.primatec.lan"
SQL_DB = "TEST_TOOL_PRE_PROD_INFRA"
PORT = "1433"

# Data directory
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

# Jira
BMW_JIRA_URL = "https://jira.cc.bmwgroup.net/"

# Reporters
REPORTERS_TABLE = "raw_jira_cc_ipnext_reporters"
PROJECTS = [
    "SWP",
    "IPNDEV",
    "IPNATH",
    "CDC",
    "ADBK25",
    "PADV",
    "ORIONINIT",
    "CVDRVN",
    "TEMINF",
]
# Filters id per department
FILTER_DEPARTMENT_MAP = {"57080": "JC", "57081": "EF", "123184": "infra_JC_EF"}
GROUPS_DEPARTMENT_MAP = {
    "swh-ext-technica-ipnext-platform-testing-ph319": "platform-testing-319",
    "swh-ext-technica-platform-testing-ph262": "platform-testing-262",
    "swh-ext-technica-ipnext-sysabs-testing-ph328": "sysabs-testing",
    "swh-ext-ltts-ipnext-platform-testing-ph318": "platform-testing-ph318",
}

# IPBM Project
IPBM_PROJECT = {
    "name": "IPBM",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "sql_table_issue": "raw_jira_cc_ipbm_daily",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# IPBD Project
IPBD_PROJECT = {
    "name": "IPBD",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_ipbd_daily",
    "sql_table_changelog": "jira_cc_ipbd_changelog",
    "sql_server": "testtooldata.primatec.lan",
    "sql_table_users": "raw_jira_cc_users",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "changelog_schema": "raw",
    "expand": "changelog",
    "author_name": "name",
    "changelog_fields": ["status"],
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Meta Data",
            "corresponding_customfield": "customfield_10700",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "team",
            "corresponding_customfield": "customfield_10115",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "variant2",
            "corresponding_customfield": "customfield_10800",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "variant3",
            "corresponding_customfield": "customfield_10801",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "project_specific_labels",
            "corresponding_customfield": "customfield_10310",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# LIGHT25 Project
LIGHT25_PROJECT = {
    "name": "Light Stack SP25",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_light25_daily",
    "sql_table_changelog": "jira_cc_light25_changelog",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "changelog_schema": "raw",
    "expand": "changelog",
    "author_name": "name",
    "changelog_fields": ["status"],
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Meta Data",
            "corresponding_customfield": "customfield_10700",
            "method_of_extraction": "field_arg_retrieval",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# SWP Project
SWP_PROJECT = {
    "name": "SWP",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_swp_daily",
    "num_update_hours": 3,
    "sql_table_sprints": "raw_jira_cc_swp_sprints",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee_display_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_name",
            "corresponding_customfield": "customfield_10105",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "external_id",
            "corresponding_customfield": "customfield_11000",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "external_ids",
            "corresponding_customfield": "customfield_10315",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "meta_data",
            "corresponding_customfield": "customfield_10700",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "DoD",
            "corresponding_customfield": "customfield_10400",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "security_level",
            "corresponding_customfield": "security",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "acceptance_criteria",
            "corresponding_customfield": "customfield_10200",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "comment",
            "corresponding_customfield": "comment",
            "method_of_extraction": "extract_simplified_comments",
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# IPNDEV Project
IPNDEV_PROJECT = {
    "name": "IPNDEV",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_ipndev_daily",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "external_ids",
            "corresponding_customfield": "customfield_10315",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# IPNATH Project
IPNATH_PROJECT = {
    "name": "IPNATH",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_ipnath_daily",
    "sql_table_sprints": "raw_jira_cc_ipnath_sprints",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee_display_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_name",
            "corresponding_customfield": "customfield_10105",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "external_ids",
            "corresponding_customfield": "customfield_10315",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "DoD",
            "corresponding_customfield": "customfield_10400",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "security_level",
            "corresponding_customfield": "security",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "acceptance_criteria",
            "corresponding_customfield": "customfield_10200",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "metadata",
            "corresponding_customfield": "customfield_10700",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "comment",
            "corresponding_customfield": "comment",
            "method_of_extraction": "extract_simplified_comments",
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# CDC Project
CDC_PROJECT = {
    "name": "CDC",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_cdc_daily",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee_display_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# ADBK25 Project
ADBK25_PROJECT = {
    "name": "ADBK25",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_adbk25_daily",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee_display_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# PADV Project
PADV_PROJECT = {
    "name": "PADV",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_padv_daily",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee_display_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

CVDRVN_PROJECT = {
    "name": "CVDRVN",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_cvdrvn_daily",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee_display_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

ORIONINIT_PROJECT = {
    "name": "ORIONINIT",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_orioninit_daily",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee_display_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

CTH_PROJECT = {
    "name": "CTH",
    "jira_url": "https://jira.technica-engineering.net/",
    "sql_table_issue": "raw_jira_technica_cth_daily",
    "sql_table_sprints": "raw_jira_technica_cth_sprints",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "Cariad_data",
    "port": "1433",
    "schema": "raw",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10501",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "project",
            "corresponding_customfield": "project",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "parent",
            "corresponding_customfield": "parent",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_id",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["id"],
        },
        {
            "field": "sprint_names",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "sprint_ids",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["id"],
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", 0],
        },
        {
            "field": "sprint_id",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["id", 0],
        },
        {
            "field": "last_sprint",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", -1],
        },
        {
            "field": "last_sprint_id",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["id", -1],
        },
        {
            "field": "linked_issues",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "original_estimate",
            "corresponding_customfield": "timeoriginalestimate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "timespent",
            "corresponding_customfield": "timespent",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "associated_ticket_number",
            "corresponding_customfield": "customfield_10208",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "story_points",
            "corresponding_customfield": "customfield_10508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "remaining_estimate",
            "corresponding_customfield": "timetracking",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["remainingEstimateSeconds"],
        },
        {
            "field": "attachment",
            "corresponding_customfield": "attachment",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["filename"],
        },
        {
            "field": "ecu",
            "corresponding_customfield": "customfield_12302",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "time_tracking",
            "corresponding_customfield": "timetracking",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["raw"],
        },
        {
            "field": "comment",
            "corresponding_customfield": "comment",
            "method_of_extraction": "extract_simplified_comments",
        },
        {
            "field": "customer_label",
            "corresponding_customfield": "customfield_17003",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "metadata",
            "corresponding_customfield": "customfield_15800",
            "method_of_extraction": "field_arg_retrieval",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

TCC_PROJECT_EXPORT = {
    "name": "TCC",
    "jira_url": "https://devstack.vwgroup.com/jira",
    "additional_conditions": ' and Type = Test and component in ("TCQ Security", "TCQ Vernetzung")'
                             ' and created >= "2024-01-01"',
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        },
        {
            "field": "changelog_history",
            "corresponding_customfield": "changelog",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["histories", False],
        },
    ],
    "list_of_fields": [
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "New KPM Tickets",
            "corresponding_customfield": "customfield_34603",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "KPM-Tickets to test",
            "corresponding_customfield": "customfield_52954",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10000",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "project",
            "corresponding_customfield": "project",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "parent",
            "corresponding_customfield": "parent",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_id",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["id"],
        },
        {
            "field": "sprint_names",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "sprint_ids",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["id"],
        },
        {
            "field": "sprints_startDate",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["startDate", 0],
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", 0],
        },
        {
            "field": "sprint_id",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["id", 0],
        },
        {
            "field": "last_sprint",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", -1],
        },
        {
            "field": "last_sprint_id",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["id", -1],
        },
        {
            "field": "timespent",
            "corresponding_customfield": "timespent",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Technology",
            "corresponding_customfield": "customfield_45200",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "Cluster",
            "corresponding_customfield": "customfield_18401",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "story_points",
            "corresponding_customfield": "customfield_10508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "SW",
            "corresponding_customfield": "customfield_31804",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "ecu",
            "corresponding_customfield": "customfield_51500",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Last comment",
            "corresponding_customfield": "customfield_19508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Acceptance Criterias name",
            "corresponding_customfield": "customfield_10335",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "Acceptance Criterias checks",
            "corresponding_customfield": "customfield_10335",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["checks"],
        },
        {
            "field": "comments_dates",
            "corresponding_customfield": "comment",
            "method_of_extraction": "extract_simplified_comments",
            "arguments": [[("created",)], False],
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

TCC_PROJECT_INGEST = {
    "name": "TCC",
    "jira_url": "https://devstack.vwgroup.com/jira",
    "sql_table_issue": "jira_vw_tcc_daily",
    "sql_table_changelog": "jira_vw_tcc_changelog",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "Cariad_data",
    "port": "1433",
    "schema": "raw",
    "changelog_schema": "raw",
    "author_name": "displayName",
    "changelog_fields": ["status", "Sprint"],
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10000",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "project",
            "corresponding_customfield": "project",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "parent",
            "corresponding_customfield": "parent",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_id",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["id"],
        },
        {
            "field": "sprint_names",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "sprint_ids",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["id"],
        },
        {
            "field": "sprints_startDate",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["startDate", 0],
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", 0],
        },
        {
            "field": "sprint_id",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["id", 0],
        },
        {
            "field": "last_sprint",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", -1],
        },
        {
            "field": "last_sprint_id",
            "corresponding_customfield": "customfield_10004",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["id", -1],
        },
        {
            "field": "timespent",
            "corresponding_customfield": "timespent",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Technology",
            "corresponding_customfield": "customfield_45200",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "Cluster",
            "corresponding_customfield": "customfield_18401",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "story_points",
            "corresponding_customfield": "customfield_10508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "SW",
            "corresponding_customfield": "customfield_31804",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "ecu",
            "corresponding_customfield": "customfield_51500",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Last comment",
            "corresponding_customfield": "customfield_19508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Acceptance Criterias name",
            "corresponding_customfield": "customfield_10335",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "Acceptance Criterias checks",
            "corresponding_customfield": "customfield_10335",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["checks"],
        },
        {
            "field": "platform_project",
            "corresponding_customfield": "customfield_52925",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "interfaces",
            "corresponding_customfield": "customfield_30903",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "new_kpm_tickets",
            "corresponding_customfield": "customfield_34603",
            "method_of_extraction": "field_arg_retrieval",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

SYSPRMGT_PROJECT = {
    "name": "SYSPRMGT",
    "jira_url": "https://jira.technica-engineering.net/",
    "expand": "worklog",
    "sql_table_issue": "raw_jira_technica_sysprmgt_daily",
    "sql_table_sprints": "raw_jira_technica_sprints",
    "sql_table_todo_list": "raw_jira_technica_sysprmgt_todo_list",
    "sql_table_worklogs": "raw_jira_technica_sysprmgt_worklogs",
    "sql_table_users": "raw_jira_technica_users",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "date_fields_format": "format_with_timezone",
    "process_str_columns": True,
    "worklogs_date_fields_format": "datetime_format",
    "to_do_field": "customfield_15101",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        },
        {
            "field": "issue_id",
            "corresponding_customfield": "id",
            "method_of_extraction": "direct_retrieval",
        },
    ],
    "list_of_fields": [
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "achieved_tcs",
            "corresponding_customfield": "customfield_13717",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "achieved_reqs",
            "corresponding_customfield": "customfield_13720",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "assignees",
            "corresponding_customfield": "customfield_10100",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "component_s",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "custom_labels",
            "corresponding_customfield": "customfield_13723",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_15109",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10501",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_name",
            "corresponding_customfield": "customfield_10503",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "project",
            "corresponding_customfield": "project",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "parent",
            "corresponding_customfield": "parent",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "story_points",
            "corresponding_customfield": "customfield_10508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "target_tl_tcs",
            "corresponding_customfield": "customfield_13716",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "team_id",
            "corresponding_customfield": "customfield_12502",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["id"],
        },
        {
            "field": "team",
            "corresponding_customfield": "customfield_12502",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "te_i_step",
            "corresponding_customfield": "customfield_15500",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "sprint_names",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "sprint_ids",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["id"],
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", 0],
        },
        {
            "field": "sprint_id",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["id", 0],
        },
        {
            "field": "kpi_estim_",
            "corresponding_customfield": "customfield_13722",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "kpi_real_",
            "corresponding_customfield": "customfield_13724",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "affected_requirement_customer_",
            "corresponding_customfield": "customfield_10207",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "bmw_crm_jira_id",
            "corresponding_customfield": "customfield_13702",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "te_project",
            "corresponding_customfield": "customfield_13602",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "attachment",
            "corresponding_customfield": "attachment",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["filename"],
        },
        {
            "field": "total_estimated_hours",
            "corresponding_customfield": "customfield_14705",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "to_do_list",
            "corresponding_customfield": "customfield_15101",
            "method_of_extraction": "extract_to_do_list",
        },
        {
            "field": "validation_name",
            "corresponding_customfield": "customfield_14907",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "customer_id",
            "corresponding_customfield": "customfield_14710",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "target_hl_tcs",
            "corresponding_customfield": "customfield_13715",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "target_hl_reqs",
            "corresponding_customfield": "customfield_13718",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "hl_amount_of_tickets",
            "corresponding_customfield": "customfield_14722",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "target_ready_tcs",
            "corresponding_customfield": "customfield_14701",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "target_refactoring_tcs",
            "corresponding_customfield": "customfield_14703",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "impacted_blocked_by",
            "corresponding_customfield": "customfield_11207",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "target_tl_reqs",
            "corresponding_customfield": "customfield_13719",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "tl_amount_of_tickets",
            "corresponding_customfield": "customfield_11807",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "achieved_ready_tcs",
            "corresponding_customfield": "customfield_14702",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "achieved_refactoring_tcs",
            "corresponding_customfield": "customfield_14704",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "achieved_tickets",
            "corresponding_customfield": "customfield_13721",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "achieved_designed_tcs",
            "corresponding_customfield": "customfield_10509",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "flagged",
            "corresponding_customfield": "customfield_10506",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "linked_issues",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "extract_simplified_links",
        },
        {
            "field": "comment",
            "corresponding_customfield": "comment",
            "method_of_extraction": "extract_simplified_comments",
        },
        {
            "field": "i_step",
            "corresponding_customfield": "customfield_11101",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "timeoriginalestimate",
            "corresponding_customfield": "timeoriginalestimate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "aggregatetimeoriginalestimate",
            "corresponding_customfield": "aggregatetimeoriginalestimate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "timespent",
            "corresponding_customfield": "timespent",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "time_tracking",
            "corresponding_customfield": "timetracking",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["raw"],
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
    ],
    "list_of_worklog_fields": [
        {
            "field": "url",
            "corresponding_customfield": "self",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "author",
            "corresponding_customfield": "author",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "updateAuthor",
            "corresponding_customfield": "updateAuthor",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "started",
            "corresponding_customfield": "started",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "comment",
            "corresponding_customfield": "comment",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "timeSpent",
            "corresponding_customfield": "timeSpent",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "timeSpentSeconds",
            "corresponding_customfield": "timeSpentSeconds",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "id",
            "corresponding_customfield": "id",
            "method_of_extraction": "field_arg_retrieval",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "started"],
    "list_float_fields": [
        "achieved_tcs",
        "achieved_reqs",
        "target_tl_tcs",
        "total_estimated_hours",
        "target_hl_tcs",
        "target_hl_reqs",
        "hl_amount_of_tickets",
        "target_ready_tcs",
        "target_refactoring_tcs",
        "target_tl_reqs",
        "tl_amount_of_tickets",
        "achieved_ready_tcs",
        "achieved_refactoring_tcs",
        "achieved_tickets",
        "achieved_designed_tcs",
        "story_points",
        "kpi_estim_",
        "kpi_real_",
    ],
}

CRMST_PROJECT = {
    "name": "CRMST",
    "jira_url": "https://jira.technica-engineering.net/",
    "sql_table_issue": "raw_jira_technica_crmst_daily",
    "sql_table_sprints": None,
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "project",
            "corresponding_customfield": "project",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "parent",
            "corresponding_customfield": "parent",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "story_points",
            "corresponding_customfield": "customfield_10508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "team",
            "corresponding_customfield": "customfield_12502",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "i_step",
            "corresponding_customfield": "customfield_15500",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "issue_id",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["id"],
        },
        {
            "field": "te_project",
            "corresponding_customfield": "customfield_13602",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "total_estimated_hours",
            "corresponding_customfield": "customfield_14705",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "customer_id",
            "corresponding_customfield": "customfield_14710",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "linked_issues",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "bmw_tpl_id",
            "corresponding_customfield": "customfield_13703",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "refactoring_of_tcs",
            "corresponding_customfield": "customfield_13710",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "implementation_of_new_tcs",
            "corresponding_customfield": "customfield_13711",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "tc_execution",
            "corresponding_customfield": "customfield_14717",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "tc_execution_in_2nd_loop",
            "corresponding_customfield": "customfield_13714",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "tc_review",
            "corresponding_customfield": "customfield_13712",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "infrastructure",
            "corresponding_customfield": "customfield_13713",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "customer_source_ticket_created_date",
            "corresponding_customfield": "customfield_14714",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "customer_source_ticket_reporter",
            "corresponding_customfield": "customfield_14713",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "comment",
            "corresponding_customfield": "comment",
            "method_of_extraction": "extract_simplified_comments",
        },
        {
            "field": "spec_review",
            "corresponding_customfield": "customfield_13709",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "new_tcs",
            "corresponding_customfield": "customfield_13708",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "changed_tcs",
            "corresponding_customfield": "customfield_13707",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "new_reqs",
            "corresponding_customfield": "customfield_13706",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "changed_reqs",
            "corresponding_customfield": "customfield_13705",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "impacted_blocked_by",
            "corresponding_customfield": "customfield_11207",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "invoiced",
            "corresponding_customfield": "customfield_17411",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "results_of_impact_analysis",
            "corresponding_customfield": "customfield_11520",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "risk_type",
            "corresponding_customfield": "customfield_17322",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "coverage_by_ready",
            "corresponding_customfield": "customfield_16807",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "coverage_by_requirements",
            "corresponding_customfield": "customfield_17318",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "final_sprint",
            "corresponding_customfield": "customfield_11910",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "attachment",
            "corresponding_customfield": "attachment",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["filename"],
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date", "final_sprint"],
    "list_float_fields": [
        "spec_review",
        "changed_reqs",
        "new_reqs",
        "changed_tcs",
        "new_tcs",
        "coverage_by_requirements",
        "coverage_by_ready",
    ],
}

# TEMINF_PROJECT
TEMINF_PROJECT = {
    "name": "TEMINF",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_teminf_daily",
    "sql_table_sprints": None,
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee_display_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "domain",
            "corresponding_customfield": "customfield_10300",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "external_id",
            "corresponding_customfield": "customfield_11000",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "external_ids",
            "corresponding_customfield": "customfield_10315",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "meta_data",
            "corresponding_customfield": "customfield_10700",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "error_occurrence",
            "corresponding_customfield": "customfield_10808",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "original_key",
            "method_of_extraction": "get_original_key",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

TDMGT_PROJECT = {
    "name": "TDMGT",
    "jira_url": "https://jira.technica-engineering.net/",
    "sql_table_issue": "raw_jira_technica_tdmgt_daily",
    "sql_table_todo_list": "raw_jira_technica_tdmgt_todo_list",
    "sql_table_sprints": None,
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "to_do_field": "customfield_14901",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "project",
            "corresponding_customfield": "project",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "parent",
            "corresponding_customfield": "parent",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "story_points",
            "corresponding_customfield": "customfield_10508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "issue_id",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["id"],
        },
        {
            "field": "linked_issues",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "comment",
            "corresponding_customfield": "comment",
            "method_of_extraction": "extract_simplified_comments",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "last_sprint",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", -1],
        },
        {
            "field": "to_do_list",
            "corresponding_customfield": "customfield_14901",
            "method_of_extraction": "extract_to_do_list",
        },

    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

TOP_PROJECT = {
    "name": "TOP",
    "jira_url": "https://jira.technica-engineering.net/",
    "sql_table_issue": "raw_jira_technica_top_daily",
    "sql_table_sprints": "raw_jira_technica_top_sprints",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["name", 0],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "project",
            "corresponding_customfield": "project",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "team",
            "corresponding_customfield": "customfield_12502",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "issue_id",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["id"],
        },
        {
            "field": "te_project",
            "corresponding_customfield": "customfield_13602",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "linked_issues",
            "corresponding_customfield": "issuelink",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "last_sprint_id",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "field_arg_retrieval_sprint",
            "arguments": ["id", -1],
        },
        {
            "field": "story_points",
            "corresponding_customfield": "customfield_10508",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "timespent",
            "corresponding_customfield": "timespent",
            "method_of_extraction": "field_arg_retrieval",
        },
    ],
    "list_of_fields_with_specific_extraction": [
        {
            "field": "remote_links",
            "method_of_extraction": "retrieve_remote_links",
        },
        {
            "field": "in_progress_history",
            "corresponding_customfield": "changelog",
            "method_of_extraction": "cast_in_progress_time_pairs_to_str",
        },
        {
            "field": "in_progress_time",
            "corresponding_customfield": "changelog",
            "method_of_extraction": "calculate_total_time_in_status",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
    "list_float_fields": ["story_points", "timespent"],
}

TXTC_PROJECT = {
    "name": "TXTC",
    "jira_url": "https://devstack.vwgroup.com/jira",
    "sql_table_issue": "jira_vw_txtc_daily",
    "sql_table_changelog": "jira_vw_txtc_changelog",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "Cariad_data",
    "port": "1433",
    "schema": "raw",
    "changelog_schema": "raw",
    "author_name": "displayName",
    "changelog_fields": ["status", "Sprint"],
    "expand": "changelog",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "project",
            "corresponding_customfield": "project",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "fix_versions",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "versions",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "kpm_tickets_to_test",
            "corresponding_customfield": "customfield_52954",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "new_kpm_tickets",
            "corresponding_customfield": "customfield_34603",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "vr",
            "corresponding_customfield": "customfield_29306",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "ecu_sw",
            "corresponding_customfield": "customfield_31804",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "ecu_hw",
            "corresponding_customfield": "customfield_31805",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "technical_solution",
            "corresponding_customfield": "customfield_23502",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "target_start",
            "corresponding_customfield": "customfield_10217",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "target_end",
            "corresponding_customfield": "customfield_10218",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "count",
            "corresponding_customfield": "customfield_38001",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "codebeamer_id",
            "corresponding_customfield": "customfield_35405",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_details",
            "corresponding_customfield": "customfield_52828",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "ecu",
            "corresponding_customfield": "customfield_30208",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "test_type",
            "corresponding_customfield": "customfield_52083",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "start_date",
            "corresponding_customfield": "customfield_10220",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "release_name",
            "corresponding_customfield": "customfield_52887",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "cluster_id",
            "corresponding_customfield": "customfield_53548",
            "method_of_extraction": "field_arg_retrieval",
        },
    ],
    "list_date_fields": [
        "created",
        "updated",
        "due_date",
        "resolution_date",
        "target_start",
        "target_end",
        "start_date",
    ],
}

# PVI Project
PVI_PROJECT = {
    "name": "PVI",
    "jira_url": "https://jira.technica-engineering.net/",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "sql_table_issue": "raw_jira_technica_pvi_daily",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10500",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "timespent",
            "corresponding_customfield": "timespent",
            "method_of_extraction": "field_arg_retrieval",
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# PTHEDL Project
PTHEDL_PROJECT = {
    "name": "PTHEDL",
    "jira_url": "https://atc.bmwgroup.net/jira",
    "sql_table_issue": "raw_jira_pthedl_daily",
    "sql_server": "testtooldata.primatec.lan",
    "sql_table_changelog": "jira_pthedl_changelog",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "raw",
    "changelog_schema": "raw",
    "expand": "changelog",
    "author_name": "displayName",
    "changelog_fields": ["assignee"],
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "parent",
            "corresponding_customfield": "parent",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "comment",
            "corresponding_customfield": "comment",
            "method_of_extraction": "extract_simplified_comments",
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10000",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10006",
            "method_of_extraction": "direct_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10001",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "test_status",
            "corresponding_customfield": "customfield_13300",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["status"],
        },
        {
            "field": "epic_name",
            "corresponding_customfield": "customfield_10003",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "assignee_name",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["displayName"],
        },
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}

# IPFSW Project
IPFSW_PROJECT = {
    "name": "IPFSW",
    "jira_url": "https://jira.cc.bmwgroup.net/",
    "sql_table_issue": "raw_jira_cc_ipfsw_daily",
    "sql_server": "testtooldata.primatec.lan",
    "sql_db": "TEST_TOOL_PRE_PROD_INFRA",
    "port": "1433",
    "schema": "dbo",
    "changelog_schema": "raw",
    "author_name": "name",
    "list_of_direct_fields": [
        {
            "field": "key",
            "corresponding_customfield": "key",
            "method_of_extraction": "direct_retrieval",
        }
    ],
    "list_of_fields": [
        {
            "field": "status",
            "corresponding_customfield": "status",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "components",
            "corresponding_customfield": "components",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "summary",
            "corresponding_customfield": "summary",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "created",
            "corresponding_customfield": "created",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "updated",
            "corresponding_customfield": "updated",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "due_date",
            "corresponding_customfield": "duedate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "other_text",
            "corresponding_customfield": "customfield_10802",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "resolution_date",
            "corresponding_customfield": "resolutiondate",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "categorization",
            "corresponding_customfield": "customfield_10304",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["value"],
        },
        {
            "field": "description",
            "corresponding_customfield": "description",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "istep",
            "corresponding_customfield": "fixVersions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "affect_version",
            "corresponding_customfield": "versions",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "priority",
            "corresponding_customfield": "priority",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "subtasks",
            "corresponding_customfield": "subtasks",
            "method_of_extraction": "list_field_retrieval_value",
            "arguments": ["key"],
        },
        {
            "field": "issue_links",
            "corresponding_customfield": "issuelinks",
            "method_of_extraction": "list_field_retrieval_in_outward_issue_type",
        },
        {
            "field": "labels",
            "corresponding_customfield": "labels",
            "method_of_extraction": "list_field_retrieval",
        },
        {
            "field": "resolution",
            "corresponding_customfield": "resolution",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "creator",
            "corresponding_customfield": "creator",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "issue_type",
            "corresponding_customfield": "issuetype",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "assignee",
            "corresponding_customfield": "assignee",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "reporter",
            "corresponding_customfield": "reporter",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        },
        {
            "field": "sprint",
            "corresponding_customfield": "customfield_10110",
            "method_of_extraction": "list_field_retrieval_sprints",
            "arguments": ["name"],
        },
        {
            "field": "number",
            "corresponding_customfield": "customfield_10900",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "story_point",
            "corresponding_customfield": "customfield_10111",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "epic_link",
            "corresponding_customfield": "customfield_10109",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "Meta Data",
            "corresponding_customfield": "customfield_10700",
            "method_of_extraction": "field_arg_retrieval",
        },
        {
            "field": "team",
            "corresponding_customfield": "customfield_10115",
            "method_of_extraction": "field_arg_retrieval_value",
            "arguments": ["name"],
        }
    ],
    "list_date_fields": ["created", "updated", "due_date", "resolution_date"],
}
