import sys
import logging

from jira_cc_ingestion.config import TCC_PROJECT_INGEST # noqa: E402
from jira_cc_ingestion.application.ingest_project_data import ingest_project_data

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
    # treat SWP project
    logger.info(f"treating {TCC_PROJECT_INGEST['name']} project...")
    ingest_project_data(token_auth, user_sql, password_sql, TCC_PROJECT_INGEST)
    logger.info(f"{TCC_PROJECT_INGEST['name']} project is treated successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise ValueError("Wrong number of argument passed.")
    token_auth = sys.argv[1]
    user_sql = sys.argv[2]
    password_sql = sys.argv[3]
    main(token_auth, user_sql, password_sql)
