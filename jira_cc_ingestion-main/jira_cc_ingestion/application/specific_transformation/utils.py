import re

import numpy as np
import pandas as pd


def datetime_diff(d2, d1):
    return round((d2 - d1).days + (d2 - d1).seconds / 86400, 2)


def nb_w_days(enddate, startdate):
    return np.busday_count(startdate, enddate)


def extract_with_contains_condition(s, contains_matching, default):
    for pattern, result in contains_matching.items():
        if pattern in s:
            return result
    return default


def extract_with_equals_condition(s, contains_matching, default):
    for pattern, result in contains_matching.items():
        if pattern == s:
            return result
    return default


def extract_betweendelimiters(s, delimter1, delimter2, occ1, occ2):
    if delimter1 not in s:
        return ""
    else:
        split1 = delimter1.join(s.split(delimter1)[occ1 + 1 :])
        if delimter2 == "":
            return split1
        if delimter2 in split1:
            return delimter2.join(split1.split(delimter2)[: occ2 + 1])
        else:
            return ""


def split_series(s, separator, n, cols):
    splited_series = s.str.strip().str.split(separator)
    splited_df = pd.concat(
        [
            splited_series.map(
                lambda str_part: int(re.sub(r"[^\d]", " ", str_part[i]).strip())
                if i < len(str_part) and re.sub(r"[^\d]", " ", str_part[i]).strip().isnumeric()
                else np.nan
            )
            for i in range(n)
        ],
        axis=1,
    )
    splited_df.columns = cols
    return splited_df


def nan_fill(n):
    return 0 if np.isnan(n) else n


def is_not_nan(n):
    return n and not (np.isnan(n))
