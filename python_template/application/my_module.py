"""Tha main pipeline."""

import logging

logger = logging.getLogger(__name__)


class MyModule:
    """Implement the main module logic."""

    @staticmethod
    def my_function() -> None:
        """Implement the main method of the class."""
        logger.info("This will be logged to console and file for my_function method")
        return None


def main():
    """Run the main entrypoint for this script used in the setup.py file."""
    MyModule.my_function()


if __name__ == "__main__":
    main()
