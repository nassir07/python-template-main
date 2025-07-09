import sys
import logging
import datetime
import pandas as pd

from jira_cc_ingestion.infra.jira import JiraData
from jira_cc_ingestion.infra.sql_db import DatabaseHelper
from jira_cc_ingestion.application.extract_from_jira import retrieve_filtered_reporters, retrieve_reporters_from_groups
from jira_cc_ingestion.config import (
    SQL_DB,
    SQL_SERVER,
    PORT,
    REPORTERS_TABLE,
    FILTER_DEPARTMENT_MAP,
    BMW_JIRA_URL,
    GROUPS_DEPARTMENT_MAP,
    PROJECTS
)

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
    # extract issues reporters that are members of some specific groups

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

    logger.info("getting current date...")
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"current date is {current_datetime}")

    logger.info(f"Retrieving reporters who are members of the configured groups...")
    extracted_reporters = retrieve_reporters_from_groups(jc, GROUPS_DEPARTMENT_MAP, PROJECTS)

    logger.info(f"Retrieving reporters from jira filters...")
    filtered_reporters = retrieve_filtered_reporters(jc.jira_connector,
                                                     filter_department_map=FILTER_DEPARTMENT_MAP)
    all_reporters = pd.concat([filtered_reporters, extracted_reporters], ignore_index=True)
    logger.info(f"Reporters Extracted!")

    logger.info("creating sql session...")
    transaction, connection = data_connector.create_session()
    logger.info("sql session is created!")

    logger.info(f"Loading reporters...")
    data_connector.delete_insert_all(connection, REPORTERS_TABLE, all_reporters)
    logger.info(f"reporters are loaded!")

    transaction.commit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise ValueError("Wrong number of argument passed.")
    token_auth = sys.argv[1]
    user_sql = sys.argv[2]
    password_sql = sys.argv[3]
    main(token_auth, user_sql, password_sql)
