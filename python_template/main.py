"""Run the main application logic."""

import logging.config
import os
import sys

from python_template.application.my_module import MyModule

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

log_config_path = os.path.join(os.path.dirname(__file__), '../log.conf')
logging.config.fileConfig(log_config_path, disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.info("Logger initialized correctly.")


def main():
    """Run the main application logic."""
    logger.info("Main function started.")
    MyModule.my_function()
    logger.info("Main function finished.")


if __name__ == "__main__":
    main()
