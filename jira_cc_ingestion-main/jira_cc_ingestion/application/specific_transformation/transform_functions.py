import datetime
import re

from jira_cc_ingestion.application.specific_transformation.utils import (
    datetime_diff,
    extract_betweendelimiters,
    extract_with_contains_condition,
    extract_with_equals_condition,
    is_not_nan,
    nan_fill,
    nb_w_days,
)


def extract_assignees_info(changelog_history, end_date, current_assignee, created_date):
    changelog_list = (
        [(created_date[:16], None)]
        + [
            (h.created, item.fromString)
            for h in changelog_history
            for item in h.items
            if item.field == "assignee"
        ]
        + [(end_date, current_assignee)]
    )
    return (
        " | ".join(
            [
                str(changelog_list[i + 1][1])
                + ":"
                + str(
                    datetime_diff(
                        datetime.datetime.strptime(changelog_list[i + 1][0][:16], "%Y-%m-%dT%H:%M"),
                        datetime.datetime.strptime(changelog_list[i][0][:16], "%Y-%m-%dT%H:%M"),
                    )
                )
                for i in range(len(changelog_list) - 1)
            ]
        ),
        datetime_diff(
            datetime.datetime.strptime(changelog_list[-1][0][:16], "%Y-%m-%dT%H:%M"),
            datetime.datetime.strptime(changelog_list[-2][0][:16], "%Y-%m-%dT%H:%M"),
        ),
        datetime.datetime.strptime(changelog_list[-2][0][:16], "%Y-%m-%dT%H:%M"),
    )


def extract_status_info(changelog_history, end_date, current_status, created_date):
    changelog_list = (
        [(created_date[:16], None)]
        + [
            (h.created, item.fromString)
            for h in changelog_history
            for item in h.items
            if item.field == "status"
        ]
        + [(end_date, current_status)]
    )
    statuses_list = [
        (
            str(changelog_list[i + 1][1]),
            datetime_diff(
                datetime.datetime.strptime(changelog_list[i + 1][0][:16], "%Y-%m-%dT%H:%M"),
                datetime.datetime.strptime(changelog_list[i][0][:16], "%Y-%m-%dT%H:%M"),
            ),
        )
        for i in range(len(changelog_list) - 1)
    ]
    return (
        datetime_diff(
            datetime.datetime.strptime(changelog_list[-1][0][:16], "%Y-%m-%dT%H:%M"),
            datetime.datetime.strptime(changelog_list[-2][0][:16], "%Y-%m-%dT%H:%M"),
        ),
        [e[1] for e in changelog_list].count("Test Blocked"),
        statuses_list,
    )


def check_daily_comments(comments_dates, start_date, end_date):
    expected_nb_comments = nb_w_days(end_date.date(), start_date.date())
    nbr_disctinct_comments_dates = len(
        set(
            [
                d.date()
                for d in comments_dates
                if start_date.date() <= d.date() and d.date() <= end_date.date()
            ]
        )
    )
    return "x" if nbr_disctinct_comments_dates > expected_nb_comments else "o"


def extract_testtype(s):
    lower_s = s.lower()
    if lower_s.startswith("ft"):
        testtype = "FT"
    elif lower_s.startswith("st"):
        testtype = "ST"
    elif lower_s.startswith("pt"):
        testtype = "PT"
    elif lower_s.startswith("dt"):
        testtype = "DT"
    elif lower_s.startswith("try"):
        testtype = "Try"
    else:
        testtype = "undefined"
    return testtype


def extract_test_iteration(s):
    test_iteration_matching = {
        "tryout": "tryout",
        "try_out": "tryout",
        "test1": "test1",
        "test2": "test2",
        "test3": "test3",
        "test4": "test4",
        "test5": "test5",
    }

    return extract_with_contains_condition(s, test_iteration_matching, "undefined")


def extract_test_system(s):
    test_system_contains_matching = {
        "CAN": "NWT",
        "FR": "NWT",
        "LIN": "NWT",
        "BAP": "BAP",
        "ETH": "BTST",
        "SOMEIP": "BTST",
        "ViWi": "BTST",
        "FAZIT": "Sec",
    }
    test_system_equals_matching = {
        "Routing": "Routing",
        "VKMS": "Sec",
        "SOK": "Sec",
        "TLS": "Sec",
        "sSOA": "Sec",
        "SOMEIP": "BTST",
        "ViWi": "BTST",
    }

    result_contains = extract_with_contains_condition(s, test_system_contains_matching, None)
    if result_contains:
        return result_contains
    else:
        extract_with_equals_condition(s, test_system_equals_matching, None)


def extract_solutiontrain(s):
    solutiontrain_contains_matching = {"ST1.1": "ST1.1", "ST1.2": "ST1.2"}
    return extract_with_contains_condition(s, solutiontrain_contains_matching, None)


def treansfrom_status(s):
    return (
        "Test performed"
        if s == "Test results ok"
        else "Failed"
        if s == "Test results not ok"
        else s
    )


def extract_yearweek(s):
    return s


def transform_epic_link(s):
    return (
        s.replace("TCC-13860", "EDAG")
        .replace("TCC-13870", "PORSCHETESTHAUS")
        .replace("TCC-13859", "DIGITEQ")
        .replace("TCC-14627", "in-tech")
        .replace("TCQ Vernetzung", "Networking")
        .replace("TCC-31666", "KPIT")
        .replace("TCC-31247", "AUDI")
        .replace("TCC-32455", "ESRLabs")
        .replace("TCQ Security", "Security")
    )


def transform_components(s):
    return s.replace("TCQ Vernetzung", "Networking").replace("TCQ Security", "Security")


def extract_kpm_extracted_list(s):
    kpm_part = extract_betweendelimiters(s, "||KPM Number||Comments if necessary||", "", 0, 1)
    kpm_part_split = [
        s.replace("KPM_", "").replace("KPM", "").strip()
        for s in "|".join(kpm_part.split("#(lf)")).split("|")
    ]
    return [
        re.search("[0-9]{6,12}", s).group().strip()
        for s in kpm_part_split
        if re.search("[0-9]{6,12}", s)
    ]


def extract_kpm_verifictaion_list(s):
    kpm_part = extract_betweendelimiters(
        s,
        "||KPM Number||Verification status (passed, failed, blocked, not tested)||KPM Ticket updated (Y/N)||Comments if not passed||",
        "",
        0,
        1,
    )
    kpm_part_split = [
        s.replace("KPM_", "").replace("KPM", "").strip()
        for s in "|".join(kpm_part.split("#(lf)")).split("|")
    ]
    return [
        re.search("[0-9]{6,12}", s).group().strip()
        for s in kpm_part_split
        if re.search("[0-9]{6,12}", s)
    ]


def extract_kpm_verifictaion_statuses(s):
    kpm_part = extract_betweendelimiters(
        s,
        "||KPM Number||Verification status (passed, failed, blocked, not tested)||KPM "
        "Ticket updated (Y/N)||Comments if not passed||",
        "",
        0,
        1,
    )
    kpm_part_split = [
        s.replace("KPM_", "").replace("KPM", "").strip().lower()
        for s in "|".join(kpm_part.split("#(lf)")).split("|")
    ]
    return [
        re.search("passed|pass|failed|fail|blocked|not tested", s).group().strip()
        for s in kpm_part_split
        if re.search("passed|pass|failed|fail|blocked|not tested", s)
    ]


def calculate_passed(r):
    if is_not_nan(r["Number of TCs CB.2"]):
        return r["passed CB.3"]
    if is_not_nan(r["passed CB.3"]):
        return r["io FEA.3"]
    if is_not_nan(r["Number of TCs FEA.2"]):
        return r["io FEA.3"]
    return r["io Raw.3"]


def calculate_failed(r):
    if is_not_nan(r["Number of TCs CB.2"]):
        return r["failed CB.4"]
    if is_not_nan(r["Number of TCs FEA.2"]):
        return r["nio FEA.4"]
    return r["nio Raw.4"]


def calculate_blocked(r):
    if is_not_nan(r["Number of TCs CB.2"]):
        return r["blocked CB.5"]
    if is_not_nan(r["Number of TCs FEA.2"]):
        return (
            nan_fill(r["Geblockt FEA.7"])
            + nan_fill(r["Testblocker FEA.6"])
            + nan_fill(r["Testfallproblem FEA.8"])
            + nan_fill(r["Testinfrastruktur FEA.9"])
        )
    return 0


def calculate_not_applicable(r):
    if is_not_nan(r["Number of TCs CB.2"]):
        return r["not applicable CB.6"]
    if is_not_nan(r["Number of TCs FEA.2"]):
        return r["abgebrochen FEA.10"] + r["offen FEA.5"]
    return nan_fill(r["nicht geplant Raw.6"]) + nan_fill(r["offen Raw.5"])


def calculate_not_run_yet(r):
    if is_not_nan(r["Number of TCs CB.2"]):
        return r["not run yet CB.7"]
    if is_not_nan(r["Number of TCs FEA.2"]):
        return 0
    return 0
