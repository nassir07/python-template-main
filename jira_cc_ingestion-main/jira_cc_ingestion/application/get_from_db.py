from datetime import timedelta
from dateutil import parser


def get_extraction_depth(data_connector, project, number_update_days=1):
    last_date = data_connector.get_last_insertion(project)
    last_date = parser.isoparse(last_date)
    if "num_update_hours" in project:
        last_date_new = last_date - timedelta(hours=project["num_update_hours"])
    else:
        last_date_new = last_date - timedelta(days=number_update_days)
    last_date_new = last_date_new.strftime("%Y-%m-%d %H:%M")
    return last_date_new


def get_todo_list_for_updated_issues(data_connector, project, list_updated_issues):
    return data_connector.get_todo_list_for_updated_issues(project, list_updated_issues)


def get_worklog_list_for_updated_issues(data_connector, project, list_updated_issues):
    return data_connector.get_worklog_list_for_updated_issues(
        project, list_updated_issues
    )


def get_last_row(
    data_connector, table_name, select_list, partition_by, order_by, deleted_columns
):
    return data_connector.get_last_row(
        table_name, select_list, partition_by, order_by, deleted_columns
    )
