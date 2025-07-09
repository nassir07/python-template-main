import datetime
import sys
import logging

from jira_cc_ingestion.application.extract_from_jira import get_commits_from_issues
from jira_cc_ingestion.infra.jira import JiraData
from jira_cc_ingestion.infra.sql_db import DatabaseHelper
from jira_cc_ingestion.infra.utils import get_active_sprint_issues
from jira_cc_ingestion.config import (
    IPBD_PROJECT,
    LIGHT25_PROJECT,
    SQL_SERVER,
    PORT,
    SQL_DB,
    BMW_JIRA_URL,
)  # noqa: E402

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M:%S",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


def main(token_auth, user_sql, password_sql):
    """main"""
    # Retrieving commits of IPBD and LIGHT25 projects issues in active sprint.
    logger.info(
        f"Retrieving commits of IPBD and LIGHT25 projects issues in active sprint..."
    )

    logger.info("connecting to sql server...")
    connection_string = "mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL+Server".format(
        user_sql, password_sql, SQL_SERVER, PORT, SQL_DB
    )
    data_connector = DatabaseHelper(connection_string=connection_string)
    logger.info("sql server is ready!")

    logger.info("connecting to jira server...")
    jc = JiraData(token=token_auth, jira_url=BMW_JIRA_URL)
    jc.connect_to_jira()
    logger.info("jira server is ready!")

    logger.info("Getting current date...")
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"current date is {current_datetime}")

    logger.info("Retrieving issues in active sprint...  ")
    jql_query = get_active_sprint_issues(
        [IPBD_PROJECT["name"], LIGHT25_PROJECT["name"]]
    )
    issues = jc.extract_jira_issues(jql_query)
    logger.info("Active sprint issues are extracted successfully!")

    logger.info("Retrieving commits of extracted issues... ")
    list_commits = [jc.get_issues_commits(issue)["commits"] for issue in issues]
    df_commits = get_commits_from_issues(list_commits, issues)
    logger.info("Commits are extracted successfully!")

    logger.info("Extracting stored commits...  ")
    transaction, connection = data_connector.create_session()
    # data_connector.insert_dataframe( connection, df_commits, 'ipb_swbk_commits')
    data_connector.update_table(
        "ipb_swbk_commits",
        connection,
        df_commits.to_dict(orient="records"),
        ["ticket", "commitId"],
    )
    connection.commit()
    logger.info(f"{IPBD_PROJECT['name']} project is treated successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise ValueError("Wrong number of argument passed.")
    token_auth = sys.argv[1]
    user_sql = sys.argv[2]
    password_sql = sys.argv[3]
    main(token_auth, user_sql, password_sql)
