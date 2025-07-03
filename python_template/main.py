"""Contain main module."""

import logging
from logging import config

from python_template.application.my_module import MyModule

# Load config
config.fileConfig("../log.conf")

# Test logging
logger = logging.getLogger(__name__)
logger.info("This will be logged to console and file")


def main():
    """Implement main function."""
    MyModule.my_function()


if __name__ == "__main__":
    main()
