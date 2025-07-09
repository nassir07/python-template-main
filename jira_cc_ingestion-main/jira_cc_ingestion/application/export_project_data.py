from jira_cc_ingestion.application.extract_from_jira import (
    retrieve_raw_issues,
    process_issues,

)

from jira_cc_ingestion.infra.jira import JiraData
import logging

logger = logging.getLogger(__name__)


def export_project_data(token_auth, project, specific_transformation=None):

    logger.info("connecting to jira server...")
    jc = JiraData(token=token_auth, jira_url=project["jira_url"])
    jc.connect_to_jira()
    logger.info("jira server is ready!")

    logger.info("getting current date...")
    server_time = jc.jira_connector.server_info()["serverTime"]
    logger.info(f"jira server time is {server_time}")

    issues_list = retrieve_raw_issues(jc, project, "2021-01-01")
    logger.info(f"update issues  and configured fields are extracted.")

    logger.info(f"Extracting of needed fields for the {project['name']} project...")
    extracted_issues = process_issues(jc, project, issues_list, server_time)
    logger.info(f"Needed fields Extracted!")

    if specific_transformation:
        logger.info(
            f"Applying specific transfromation for the {project['name']} project..."
        )
        transformed_issues = specific_transformation(
            extracted_issues, server_time=server_time
        )
        logger.info(f"Needed fields Extracted!")
        return transformed_issues, server_time[:10]
    return extracted_issues, server_time[:10]



