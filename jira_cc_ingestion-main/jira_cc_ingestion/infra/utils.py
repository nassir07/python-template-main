import re
from datetime import datetime, timedelta


def transform_column_names(df):
    """Define a function to clean column names"""

    def clean_column_name(name):
        name = re.sub(r"\W+", "_", name)
        return name.lower()

    # Apply the clean_column_name function to each column name
    df.columns = [clean_column_name(col) for col in df.columns]
    return df


def truncate_dataframe_columns(df, max_length=10000):
    """truncate dataframe columns"""

    def truncate_text(text):
        # Check if the value is a string before truncating
        if type(text) == str:
            # Truncate the string if it's longer than max_length
            if len(text) > max_length:
                return text[:max_length]
            return text
        # Return the value as is if it's not a string
        return text

    new_df = df.copy()  # Create a copy of the original DataFrame

    # Apply the truncate_text function to each cell in the DataFrame
    for col in new_df.columns:
        new_df[col] = new_df[col].apply(truncate_text)
    return new_df


def extract_sprint_names(input_string):
    """Use regular expression to extract the name(s)"""
    sprint_names = ",".join(re.findall(r"name=(.*?),", input_string))
    return sprint_names


def extract_sprint_ids(input_string):
    """Use regular expression to extract the id(s)"""
    sprint_ids = ",".join(re.findall(r"id=(.*?),", input_string))
    return sprint_ids


def extract_first_sprint_id(input_string):
    return input_string.split(",")[0] if input_string else None


def extract_first_sprint_name(input_string):
    return input_string.split(",")[0] if input_string else None


def extract_simplified_link(link):
    id = link["id"]
    if "inwardIssue" in link:
        link_type = link["type"]["inward"]
        linked_issue = link["inwardIssue"]["key"]
    else:
        link_type = link["type"]["outward"]
        linked_issue = link["outwardIssue"]["key"]
    return ",".join((id, link_type, linked_issue))


def extract_simplified_links(links):
    if len(links) == 0:
        return None
    return "(" + "),(".join([extract_simplified_link(link) for link in links]) + ")"


def extract_simplified_comment(comment):
    id = comment["id"]
    author = comment["author"]["name"]
    body = comment["body"]
    updated = comment["updated"]

    return "|".join((id, author, body, updated))


def extract_simplified_comments(comments):
    if len(comments["comments"]) == 0:
        return None
    return (
        "("
        + "),(".join(
            [extract_simplified_comment(comment) for comment in comments["comments"]]
        )
        + ")"
    )


def get_active_sprint_issues(list_projects_name):
    jql_query = {
        "text": 'project in ("{}") and Sprint in openSprints() And Sprint = "{}" and (summary  ~"{}" or '
        'summary  ~"{}" )',
        "arguments": [
            '","'.join(list_projects_name),
            "swbk",
            "implementation",
            "Execution",
        ],
    }
    return jql_query


WORK_START = 9  # 9 AM
WORK_END = 18   # 6 PM


def is_within_working_hours(dt: datetime) -> bool:
    """Check if the given datetime is within working hours (9 AM to 6 PM)."""
    WORK_START = 9  # 9 AM
    WORK_END = 18  # 6 PM
    return WORK_START <= dt.hour < WORK_END


def calculate_working_hours(start: datetime, end: datetime) -> timedelta:
    """Calculate the time spent within working hours (9 AM to 6 PM)."""
    # If start or end is outside working hours, adjust it to 9 AM or 6 PM
    WORK_START = 9  # 9 AM
    WORK_END = 18  # 6 PM
    if start.hour < WORK_START:
        start = start.replace(hour=WORK_START, minute=0, second=0, microsecond=0)
    if end.hour >= WORK_END:
        end = end.replace(hour=WORK_END, minute=0, second=0, microsecond=0)

    # Skip if the start time is after the end time or both are outside working hours
    if start >= end:
        return timedelta()

    # Calculate total time spent within working hours
    total_duration = timedelta()

    # If start and end are on the same day and within working hours, calculate the difference
    if start.date() == end.date():
        total_duration = end - start
    else:
        # Calculate time for the start day (from start to 6 PM)
        start_end_of_day = start.replace(hour=WORK_END, minute=0, second=0, microsecond=0)
        total_duration += start_end_of_day - start

        # Calculate time for the end day (from 9 AM to end)
        end_start_of_day = end.replace(hour=WORK_START, minute=0, second=0, microsecond=0)
        total_duration += end - end_start_of_day

        # For multi-day spans, we'll need to add full working days between the start and end
        current_day = start.date() + timedelta(days=1)
        while current_day < end.date():
            day_start = datetime.combine(current_day, datetime.min.time()).replace(hour=WORK_START)
            day_end = datetime.combine(current_day, datetime.min.time()).replace(hour=WORK_END)
            total_duration += day_end - day_start
            current_day += timedelta(days=1)

    return total_duration
