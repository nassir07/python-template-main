import pandas as pd
from sqlalchemy import create_engine, text, inspect, Table, tuple_, delete, MetaData
from sqlalchemy.orm import sessionmaker


class DatabaseHelper:
    def __init__(self, connection_string, schema=None):
        """Initialize the class with a database connection using the provided connection string"""
        self.schema = schema
        self.engine = create_engine(
            connection_string, echo=False, use_setinputsizes=False
        )
        session_object = sessionmaker(bind=self.engine)
        self.session = session_object()
        self.inspector = inspect(self.engine)
        self.metadata = MetaData()

    def create_table(self, dataframe, table_name):
        """Create a table in the database using the provided dataframe"""
        dataframe.to_sql(table_name, self.engine, if_exists="append", index=False)

    def read_data(self, table_name):
        """Read data from the specified table and return it as a dataframe"""
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql(query, self.engine)
        return data

    def insert_dataframe(self, connection, dataframe, table_name):
        """Insert data from the provided dataframe into the specified table"""
        dataframe.to_sql(table_name, connection, if_exists="append", index=False)

    def get_last_insertion(self, project):
        query = f"SELECT TOP(1) updated FROM {project['sql_table_issue']} order by updated desc "
        data = pd.read_sql(query, self.engine)
        return str(data["updated"][0])

    def get_last_row(
        self, table_name, select_list, partition_by, order_by, deleted_columns
    ):
        conditions = [f"({col} = 0 OR {col} IS NULL)" for col in deleted_columns]
        where_clause = " AND ".join(conditions)
        query = (
            f"select * from (Select {', '.join(select_list)}, ROW_NUMBER() OVER (PARTITION BY {', '.join(partition_by)} ORDER BY "
            f"[{order_by}] DESC) AS row_num from  {table_name} "
            f"where {where_clause} ) t where t.row_num = 1"
        )
        data = pd.read_sql(query, self.engine)
        return data

    def get_todo_list_for_updated_issues(self, project, list_updated_issues):
        str_list_issues = "'" + "','".join(list_updated_issues) + "'"
        query = (
            f"select * from (select *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY date_of_insert DESC) AS "
            f"row_num from {project['sql_table_todo_list']}) TP where TP.row_num = 1 and TP.issue_id in ( "
            f"{str_list_issues}) and (TP.todo_is_deleted = 0 or TP.todo_is_deleted is null)   "
            f"and (TP.issue_is_deleted = 0 or TP.issue_is_deleted is null)"
        )
        data = pd.read_sql(query, self.engine)
        return data

    def get_worklog_list_for_updated_issues(self, project, list_updated_issues):
        str_list_issues = "'" + "','".join(list_updated_issues) + "'"
        query = (
            f"select * from (select *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated DESC) AS "
            f"row_num from {project['sql_table_worklogs']}) TP where TP.row_num = 1 and TP.issue_id in ( "
            f"{str_list_issues}) and (TP.worklog_is_deleted = 0 or TP.worklog_is_deleted is null)   "
            f"and (TP.issue_is_deleted = 0 or TP.issue_is_deleted is null)"
        )
        data = pd.read_sql(query, self.engine)
        return data

    def delete_insert_all(self, connection, table_name, data):
        if self.inspector.has_table(table_name):
            connection.execute(text(f"DELETE FROM {table_name}"))
            data.to_sql(table_name, connection, if_exists="append", index=False)
        else:
            data.to_sql(table_name, connection, if_exists="append", index=False)

    def get_data_from_query(self, connection, query_text):
        data = pd.read_sql(query_text, connection)
        return data

    def update_table(
        self,
        table_name,
        connection,
        data_list,
        unique_keys_list,
        source_colnames_mapping=dict(),
    ):
        """Doing an UPDATE SQL operation, if a particular row already exists, it will be updated with new values.

        :param str table_name: The name of the table SQL that will be updated
        :param list data_list: A list of dict containing the data to insert
        :param list unique_keys_list: A list of keys, based on them a row is considered as existed or not
        :param dict source_colnames_mapping: A dict containing a mapping between the keys of the rows that we will be upserted and the columns names.
        """
        if data_list and unique_keys_list:
            keys = list(data_list[0].keys())
            keys_string_target = ", ".join(
                "[" + source_colnames_mapping.get(key, key) + "]" for key in keys
            )
            keys_string_source = ", ".join(key for key in keys)

            keys_values_string = ":" + ", :".join(keys)
            on_string = " and ".join(
                [
                    "target.["
                    + source_colnames_mapping.get(key, key)
                    + "] = source."
                    + key
                    for key in unique_keys_list
                ]
            )
            insert_string = (
                "("
                + keys_string_target
                + ") VALUES ("
                + ", ".join(["source." + key for key in keys])
                + ")"
            )
            keys = [item for item in keys if item not in unique_keys_list]
            update_string = ", ".join(
                [
                    "[" + source_colnames_mapping.get(key, key) + "] = source." + key
                    for key in keys
                ]
            )

            stmt = text(
                f"""
                MERGE INTO {table_name} AS target
                USING (VALUES ({keys_values_string})) AS source ({keys_string_source})
                ON {on_string}
                WHEN MATCHED THEN 
                    UPDATE SET {update_string}
                WHEN NOT MATCHED THEN 
                    INSERT {insert_string};
            """
            )
            connection.execute(stmt, data_list)

    def delete_insert(self, connection, table_name: str, schema, data_list: list, unique_keys_list: list,
                      source_colnames_mapping: dict = dict()):
        """Combines an UPDATE and an INSERT SQL operation, if a particular row already exists, it will be updated with new values and if it does not exist.
        If it doesn't exist, a new row will be inserted.

        :param str table_name: The name of the SQL table.
        :param list data_list: A list of dict containing the data that will be upserted.
        :param list unique_keys_list: A list of column names, based on them a row is considered as existed or not
        :param optional dict source_colnames_mapping: A dict containing a mapping between the keys of the rows that will be upserted and the columns names.
        """
        table = Table(table_name, self.metadata, schema=schema, autoload_with=self.engine)
        unique_data_keys = [source_colnames_mapping[key] for key in unique_keys_list]
        keys_to_delete = [tuple(record[key] for key in unique_data_keys) for record in data_list]
        for i in range(0, len(keys_to_delete), 100):
            delete_stmt = (
                    delete(table).
                    where(tuple_(*[getattr(table.c, key) for key in unique_data_keys]).in_(
                        keys_to_delete[i:i+100])))
            connection.execute(delete_stmt)
        data_to_insert = [{source_colnames_mapping.get(key, key): value for key, value in record.items()}
                          for record in data_list]
        for i in range(0, len(data_to_insert), 100):
            insert_stmt = table.insert().values(data_to_insert[i:i+100])
            connection.execute(insert_stmt)

    def create_session(self):
        """create a sql server session"""
        connection = self.engine.connect()
        transaction = connection.begin()
        return transaction, connection
