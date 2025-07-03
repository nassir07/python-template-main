"""Implement a class used to communicate with dbs."""

import logging

import pandas as pd
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)


class DatabaseHelper:
    """Implement a class used to communicate with dbs."""

    def __init__(self, sql_sever, sql_db, port, user_sql, password_sql):
        """Initiate the class instance."""
        connection_string = "mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL+Server".format(user_sql, password_sql, sql_sever, port, sql_db)
        self.engine = create_engine(connection_string, use_setinputsizes=False)

    def create_table(self, dataframe, table_name, if_exists="append"):
        """Create a table."""
        dataframe.to_sql(table_name, self.engine, if_exists=if_exists, index=False)

    def read_data(self, table_name, selected_columns=None):
        """Read data from a table with specified columns."""
        query = f"SELECT * FROM {table_name}" if selected_columns else f"SELECT {', '.join(selected_columns)} FROM {table_name}"
        data = pd.read_sql(query, self.engine)
        return data

    def insert_dataframe(self, dataframe, table_name):
        """Insert data into a table from a pandas dataframe."""
        dataframe.to_sql(table_name, self.engine, if_exists="append", index=False)
