import pandas as pd
import numpy as np

from jira_cc_ingestion.application.utils import (
    format_date,
    rectify_year_in_datetime,
    replace_characters,
    process_df_columns,
)


def delete_insert_sprints_data(data_connector, connection, sprints_data, table_name):
    data_connector.delete_insert_all(connection, table_name, pd.DataFrame(sprints_data))


def delete_insert_users_data(data_connector, connection, users_data, table_name):
    data_connector.delete_insert_all(connection, table_name, pd.DataFrame(users_data))


def update_changelog_data(data_connector, connection, changelog_data, table_name, schema):
    data_connector.delete_insert(connection, table_name, schema, changelog_data, unique_keys_list=["key"],
                                 source_colnames_mapping={"key": "key"})


def tag_deleted(
    data_connector, connection, keys_to_tag, table, keys_column, deleted_column
):
    data_list = [{"key_str": key, deleted_column: 1} for key in keys_to_tag]

    data_connector.update_table(
        table, connection, data_list, ["key_str"], {"key_str": keys_column}
    )


def loading_deleted_todo(
    data_connector, connection, project, df_todo_list_were_deleted, date_of_insert
):
    df_todo_list_were_deleted["date_of_insert"] = date_of_insert
    data_connector.insert_dataframe(
        connection, df_todo_list_were_deleted, project["sql_table_todo_list"]
    )


def loading_deleted_worklog(
    data_connector, connection, project, df_worklog_list_were_deleted, date_of_insert
):
    df_worklog_list_were_deleted["updated"] = date_of_insert
    data_connector.insert_dataframe(
        connection, df_worklog_list_were_deleted, project["sql_table_worklogs"]
    )


def loading_info(
    data_connector,
    connection,
    table_name,
    extracted_data,
    existent_data,
    key_columns,
    date_fields=None,
    date_fields_format=None,
    process_str_columns=False,
    float_fields=None
):
    if not extracted_data.empty:
        if process_str_columns:
            extracted_data = prepare_str_columns_for_sql_statement(extracted_data)
        if date_fields and date_fields_format != "format_with_timezone":
            existent_data["updated"] = existent_data["updated"].dt.strftime('%Y-%m-%d %H:%M:%S')
            existing_date_fields = [
                col for col in date_fields if col in extracted_data.columns
            ]
            extracted_data[existing_date_fields] = extracted_data[
                existing_date_fields
            ].applymap(format_date)
        filtered_df = filter_data(extracted_data, existent_data, key_columns)
        if float_fields:
            for col in float_fields:
                filtered_df[col] = filtered_df[col].map(
                    lambda x: None if np.isinf(pd.to_numeric(x, errors='coerce')) else pd.to_numeric(x, errors='coerce')
                )
        unique_filtered_df = filtered_df.drop_duplicates(subset=key_columns, keep='first')
        data_connector.insert_dataframe(connection, unique_filtered_df, table_name)


def filter_data(extracted_data, existent_data, key_columns):
    existent_keys = set(existent_data[key_columns].itertuples(index=False, name=None))
    filtered_df = extracted_data[
        [
            key_tuple not in existent_keys
            for key_tuple in extracted_data[key_columns].itertuples(
                index=False, name=None
            )
        ]
    ]
    return filtered_df


def prepare_str_columns_for_sql_statement(
    df, str_columns=["comment"], dt_columns=["started"]
):
    df_prepared = process_df_columns(
        df, str_columns, lambda s: replace_characters(s, ["'", '"'], " ")
    )
    df_prepared = process_df_columns(df_prepared, dt_columns, rectify_year_in_datetime)
    return df_prepared
