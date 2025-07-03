"""Config module."""

import os

from dotenv import load_dotenv

load_dotenv()

# Sql server
MSSQL_SERVER = "SQL_SERVER"
MSSQL_DB = "DB"
PORT = "1433"
MSSQL_USER = os.environ["MSSQL_USER"]
MSSQL_PW = os.environ["MSSQL_PW"]

# Jenkins servers
JENKINS_SERVERS = [
    {
        "name": "jenkins2",
        "hostname": "jenkins2.technica-engineering.net/",
        "token": os.environ["JENKINS2_TOKEN"],
    },
    {
        "name": "jenkins6",
        "hostname": "jenkins6.technica-engineering.net/",
        "token": os.environ["JENKINS6_TOKEN"],
    },
]

# JIRA TECHNICA
JIRA_TECHNICA_SERVER = "https://jira.technica-engineering.net/"
JIRA_TECHNICA_TOKEN = os.environ["JIRA_TECHNICA_TOKEN"]

# Technical user
TECHNICAL_USER = "username"
TECHNICAL_USER_PASSWORD = os.environ["TECHNICAL_USER_PASSWORD"]
TECHNICAL_USER_TOKEN = os.environ["TECHNICAL_USER_TOKEN"]
