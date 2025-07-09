import os
import sys
import logging

from jira_cc_ingestion.application import utils
from jira_cc_ingestion.application.export_project_data import export_project_data
from jira_cc_ingestion.application.specific_transformation.transform_tcc_data import (
    transform_tcc_data,
)
from jira_cc_ingestion.config import DATA_DIR, TCC_PROJECT_EXPORT  # noqa: E402
from jira_cc_ingestion.infra.write_excel import write_excel

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M:%S",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


def main(token_auth):
    """main"""
    # treat CTH project
    utils.check_create_dir(DATA_DIR)
    logger.info(f"treating {TCC_PROJECT_EXPORT['name']} project...")
    exported_data, file_time = export_project_data(
        token_auth,
        TCC_PROJECT_EXPORT,
        specific_transformation=transform_tcc_data,
    )
    logger.info(f"writing  {TCC_PROJECT_EXPORT['name']} data to disk...")
    percentage_cols = ("Percentage of not aborted / executed TCs", "Percentage of passed applicable TCs",
                       "Percentage time in Deffect Discussion", "Testcoverage (passed+failed)/ applicable")
    write_excel(exported_data, os.path.join(DATA_DIR, f"IntegrityCriteria_{file_time}.xlsx"),
                "IC_All_Status_All_Sprints", {percentage_cols: {"num_format": "0%"}},
                {
                    ('Test Result in Analysis', 'Defects Discussion'): {
                        'format': {"bg_color": "#FF0000"},
                        'type': "cell",
                        'criteria': ">",
                        'value': 7
                    },
                    ('Test in Documentation',): {
                        'format': {"bg_color": "#FF0000"},
                        'type': "cell",
                        'criteria': ">",
                        'value': 3

                    }

                })
    logger.info(f"{TCC_PROJECT_EXPORT['name']} project is treated successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Wrong number of argument passed.")
    token_auth = sys.argv[1]
    main(token_auth)
