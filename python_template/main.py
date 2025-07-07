"""Contain main module."""

import logging.config
import os
import sys

from python_template.application.my_module import MyModule

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 1. Construire le chemin absolu vers log.conf
log_config_path = os.path.join(os.path.dirname(__file__), '../log.conf')

# 2. Charger la configuration de logging
logging.config.fileConfig(log_config_path, disable_existing_loggers=False)

# 3. Créer le logger
logger = logging.getLogger(__name__)
logger.info("Logger initialized correctly.")


def main():
    """Main entry point of the application."""
    logger.info("Main function started.")
    MyModule.my_function()
    logger.info("Main function finished.")


if __name__ == "__main__":
    main()


