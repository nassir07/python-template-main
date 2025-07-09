from datetime import datetime, timedelta

from jira_cc_ingestion.infra.utils import calculate_working_hours


def direct_retrieval(raw_field_value):
    """direct_retrieval"""
    return raw_field_value


def list_field_retrieval_value(raw_field_value, key):
    """list_field_retrieval_value"""
    if raw_field_value is None:
        return ""
    else:
        return ", ".join([vars(element).get(key, "") for element in raw_field_value])


def field_arg_retrieval_value(raw_field_value, key, to_str=True):
    """field_arg_retrieval_value"""
    if raw_field_value is None:
        return ""
    if to_str:
        return str(vars(raw_field_value).get(key, ""))
    else:
        return vars(raw_field_value).get(key, "")


def field_arg_retrieval(raw_field_value):
    """field_arg_retrieval"""
    if raw_field_value is None:
        return ""
    else:
        return raw_field_value


def list_field_retrieval(raw_field_value):
    """list_field_retrieval"""
    if raw_field_value is None:
        return ""
    else:
        return ", ".join([element for element in raw_field_value])


def list_field_retrieval_in_outward_issue_type(raw_field_value):
    """Extracts issue links and assigns the correct relationship type."""
    if raw_field_value is None:
        return ""

    list_links = []
    for element in raw_field_value:
        element_dict = vars(element)

        if "outwardIssue" in element_dict:  # Check if outwardIssue exists
            list_links.append(f"{element.outwardIssue.key} : {element.type.outward}")
        elif "inwardIssue" in element_dict:  # Check if inwardIssue exists
            list_links.append(f"{element.inwardIssue.key} : {element.type.inward}")

    return ", ".join(list_links)


def extract_simplified_link(link):
    id = link.id
    if "inwardIssue" in vars(link):
        link_type = link.type.inward
        linked_issue = link.inwardIssue.key
    else:
        link_type = link.type.outward
        linked_issue = link.outwardIssue.key
    return ",".join((id, link_type, linked_issue))


def extract_simplified_links(links):
    if len(links) == 0:
        return ""
    return "(" + "),(".join([extract_simplified_link(link) for link in links]) + ")"


def list_field_retrieval_sprints(raw_field_value, key):
    """list_field_retrieval_sprints_info"""
    if raw_field_value is None:
        return ""
    else:
        return ", ".join([element.split(key + "=")[1].split(",")[0] for element in raw_field_value])


def field_arg_retrieval_sprint(raw_field_value, key, pos):
    """list_field_retrieval_sprint_info"""
    if raw_field_value is None:
        return ""
    else:
        return raw_field_value[pos].split(key + "=")[1].split(",")[0]


def extract_simplified_comment(
    comment, list_fields=[("id",), ("author", "name"), ("body",), ("updated",)]
):
    extracted_field = [comment.raw[field[0]] for field in list_fields]
    return "|".join(
        [
            extracted_field[i][field[1]] if len(field) > 1 else extracted_field[i]
            for i, field in enumerate(list_fields)
        ]
    )


def extract_simplified_comments(
    comments, list_fields=[("id",), ("author", "name"), ("body",), ("updated",)], to_str=True
):
    if len(vars(comments)["comments"]) == 0:
        return ""
    if to_str:
        return (
            "("
            + "),(".join(
                [
                    extract_simplified_comment(comment, list_fields)
                    for comment in vars(comments)["comments"]
                ]
            )
            + ")"
        )
    else:
        return [
            extract_simplified_comment(comment, list_fields)
            for comment in vars(comments)["comments"]
        ]


def get_original_key(**kwargs):
    issue = kwargs["issue"]
    i = 0
    histories = issue.changelog.histories
    while i < len(histories):
        items = histories[i].items
        j = 0
        while j < len(items):
            if items[j].field == "Key":
                return items[j].fromString
            j += 1
        i += 1
    return ""


def retrieve_remote_links(**kwargs):
    issue = kwargs["issue"]
    jc = kwargs["jc"]
    remote_links = jc.jira_connector.remote_links(issue.key)
    return " ,".join(
        [
            link.raw["object"]["url"]
            for link in remote_links
            if link.raw["object"]["title"] == "jenkins job"
        ]
    )


def extract_in_progress_date_pairs(**kwargs):
    """
    Extracts pairs of dates for changes into and out of 'In Progress'.

    Parameters:
    changelog (List[dict]): A list of dictionaries containing changelog data.
        Each dictionary represents a changelog entry with 'timestamp', 'field', 'fromString', and 'toString'.

    Returns:
    List[Tuple[str, Optional[str]]]: A list of tuples, where each tuple contains:
                                      - Start date/time when 'In Progress' began.
                                      - End date/time when 'In Progress' ended (or None if it hasn't ended).
    """

    issue = kwargs["issue"]
    changelog = issue.changelog
    date_pairs = []
    start_date = None  # To track the start of "In Progress"

    # Loop through each change in the changelog
    for change in changelog.histories:
        for item in change.items:
            if item.field == "status":
                # If the status changes to "In Progress"
                if item.toString == "In Progress":
                    start_date = change.created
                # If the status changes from "In Progress"
                elif item.fromString == "In Progress":
                    if start_date:  # Ensure there was a start before the end
                        date_pairs.append((start_date, change.created))
                        start_date = None  # Reset start_date after pairing

    # If there's an unclosed "In Progress" period, add it with None as the end date
    if start_date:
        date_pairs.append((start_date, None))
    return date_pairs


def calculate_total_time_in_status(**kwargs):
    # Extract the date pairs
    date_pairs = extract_in_progress_date_pairs(**kwargs)
    # Calculate the total time spent
    total_duration = timedelta()
    for start, end in date_pairs:
        start_dt = datetime.fromisoformat(start[:-5])
        end_dt = datetime.fromisoformat(end[:-5]) if end else datetime.now()
        # Calculate the time spent during working hours
        total_duration += calculate_working_hours(start_dt, end_dt)
    return total_duration // timedelta(minutes=1)


def cast_in_progress_time_pairs_to_str(**kwargs):
    date_paris = extract_in_progress_date_pairs(**kwargs)
    return str(date_paris)


def extract_to_do_list(raw_field_value):
    """field_arg_retrieval"""
    if raw_field_value is None:
        return ""
    else:
        todo_list_content = [extract_to_do_item(d) for d in raw_field_value if d.todo != "[]"]
        return str(todo_list_content) if todo_list_content else None


def extract_to_do_item(to_do_item):
    """field_arg_retrieval"""
    todo_item_content = vars(to_do_item)
    if "status" in todo_item_content:
        todo_item_content["status"] = todo_item_content["status"].name
    return todo_item_content
