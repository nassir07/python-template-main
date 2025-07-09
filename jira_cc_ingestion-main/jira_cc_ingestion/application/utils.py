import os
from datetime import datetime
import numpy as np
import pandas as pd
from dateutil import parser


def check_create_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def replace_characters(input_str, to_replace, replacement):
    """replace characters in the to_replace list of str with the replacement str"""
    result_str = input_str
    for s in to_replace:
        result_str = result_str.replace(s, replacement)
    return result_str


def rectify_year_in_datetime(input_str):
    """rectify year avlue in a datetime str"""
    result_dt = parser.isoparse(input_str).strftime("%Y-%m-%d %H:%M:%S")
    result_dt = datetime.strptime(result_dt, "%Y-%m-%d %H:%M:%S")
    if (result_dt.year < 1900) or (result_dt.year >= 2100):
        result_dt = result_dt.replace(year=datetime.now().year)
    return result_dt.strftime("%Y-%m-%d %H:%M:%S")


def process_df_columns(df, str_columns, processing_func):
    """return a deep copy of a dataframe and apply a processing function on a given list of columns"""
    result_df = df.copy(deep=True)
    for col in str_columns:
        if col in result_df:
            result_df[col] = result_df[col].replace({np.nan: None})
            result_df[col] = result_df[col].map(
                lambda x: processing_func(x) if x else x
            )
    return result_df


# Function to format date
def format_date(date_str):
    if not date_str:
        return None
    dt = pd.to_datetime(date_str)
    rounded_next_minute = dt.ceil('T').strftime('%Y-%m-%d %H:%M:%S') if dt.second >= 30 \
        else dt.floor('T').strftime('%Y-%m-%d %H:%M:%S')

    MIN_SMALLDATETIME = '1900-01-01 00:00'
    MAX_SMALLDATETIME = '2079-06-06 00:00'

    return max(MIN_SMALLDATETIME, min(rounded_next_minute, MAX_SMALLDATETIME))


# Function to join the values within each list
def join_list(lst):
    return ", ".join(map(str, lst))
