import pandas as pd

from jira_cc_ingestion.application.specific_transformation.transform_functions import *
from jira_cc_ingestion.application.specific_transformation.utils import (
    nan_fill,
    nb_w_days,
    split_series,
)


INITIAL_COLUMNS = [
    "summary",
    "key",
    "sprint_names",
    "SW",
    "TestType",
    "test iteration",
    "ecu",
    "Technology",
    "test system",
    "Tech-Cluster",
    "Custom field (Epic Link)",
    "Solution Train",
    "Cluster",
    "Current teststatus",
    "time in current status",
    "assignee",
    "time with current Assignee",
    "Assignee history",
    "was blocked?",
    "Erstdurchdringung",
    "created [year/week]",
    "resolution_date",
    "resolved [year/week]",
    "Testcoverage (passed+failed)/ applicable",
    "Total applicable TCs",
    "passed",
    "failed",
    "blocked",
    "not_applicable",
    "not run yet",
    "Results table filled",
    "Jira ticket correct filled",
    "Logfile available",
    "Codebeamer Excels/FEAs available",
    "KPMs finished",
    "DailyCommentCheck",
    "Test-Bug Tickets created",
    "Percentage of not aborted / executed TCs",
    "Percentage of passed applicable TCs",
    "Planned",
    "Backlog",
    "Accepted for Implementation",
    "In Progress",
    "Waiting",
    "In Analysis",
    "Implementation Review",
    "Provide Documentation",
    "Test Blocked",
    "Total",
    "Total excluding Blocked/Planned",
    "Percentage time in Deffect Discussion",
    "#Problems",
    "#Summary",
    "#Links",
    "KPMs created list",
    "KPMs created count",
    "KPMs verification list",
    "KPMs verification statuses",
    "KPMs verification status count passed|failed|blocked|not tested",
]

TARGET_COLUMNS = [
    "Summary",
    "TCC",
    "Sprint",
    "SW",
    "Test Type",
    "Test Iteration",
    "ECU",
    "Technology",
    "Test system",
    "Tech-Cluster",
    "Trade",
    "Solution Train",
    "Cluster",
    "Current teststatus",
    "time in current status",
    "current Assignee",
    "time with current Assignee",
    "Assignee history",
    "was blocked?",
    "first coverage? (Erstdurchdringung)",
    "created [year/week]",
    "resolved",
    "resolved [year/week]",
    "Testcoverage (passed+failed)/ applicable",
    "Total applicable TCs",
    "passed",
    "failed",
    "blocked",
    "not applicable",
    "not run yet",
    "Results table filled",
    "Jira ticket correct filled",
    "Logfile available",
    "Codebeamer Excels/FEAs available",
    "KPMs finished",
    "Daily comments",
    "Test-Bug Tickets created",
    "Percentage of not aborted / executed TCs",
    "Percentage of passed applicable TCs",
    "Planned",
    "Backlog",
    "Test in Preparation",
    "Test Running",
    "Waiting",
    "Test Result in Analysis",
    "Defects Discussion",
    "Test in Documentation",
    "Test Blocked",
    "Total",
    "Total excluding Blocked/Planned",
    "Percentage time in Deffect Discussion",
    "#Problems",
    "#Summary",
    "#Links",
    "KPMs created list",
    "KPMs created count",
    "KPMs verification list",
    "KPMs verification statuses",
    "KPMs verification status count passed|failed|blocked|not tested",
]


def transform_tcc_data(extracted_issues, server_time):
    extracted_issues["end date"] = extracted_issues["resolution_date"].map(
        lambda d: (
            datetime.datetime.strptime(d[:16], "%Y-%m-%dT%H:%M")
            if d
            else datetime.datetime.strptime(server_time[:16], "%Y-%m-%dT%H:%M")
        )
    )
    extracted_issues["created"] = pd.to_datetime(extracted_issues["created"].str[:16])
    assignee_extracted_info = extracted_issues.apply(
        lambda r: extract_assignees_info(
            r["changelog_history"],
            r["end date"].strftime("%Y-%m-%dT%H:%M"),
            r["assignee"],
            r["created"].strftime("%Y-%m-%dT%H:%M"),
        ),
        axis=1,
    )
    extracted_issues["Assignee history"] = [l[0] for l in assignee_extracted_info]
    extracted_issues["time with current Assignee"] = [
        l[1] for l in assignee_extracted_info
    ]
    extracted_issues["Current assignee date"] = [l[2] for l in assignee_extracted_info]
    status_extracted_info = extracted_issues.apply(
        lambda r: extract_status_info(
            r["changelog_history"],
            r["end date"].strftime("%Y-%m-%dT%H:%M"),
            r["status"],
            r["created"].strftime("%Y-%m-%dT%H:%M"),
        ),
        axis=1,
    )
    extracted_issues["time in current status"] = [round(l[0], 1) for l in status_extracted_info]
    extracted_issues["Status_Blocked_Counter"] = [l[1] for l in status_extracted_info]
    extracted_issues["was blocked?"] = extracted_issues["Status_Blocked_Counter"].map(
        lambda x: "x" if x > 0 else "o"
    )
    statuses_list = [
        "Planned",
        "Backlog",
        "Test Blocked",
        "Accepted for Implementation",
        "Cancelled",
        "Test results ok",
        "Implementation Review",
        "In Analysis",
        "Waiting",
        "Provide Documentation",
        "In Progress",
        "Test results not ok",
    ]
    for status in statuses_list:
        extracted_issues[status] = [
            round(sum([e[1] for e in l[2] if e[0] == status]), 1)
            for l in status_extracted_info
        ]
    extracted_issues["Total"] = (
        extracted_issues[
            [
                "Planned",
                "Backlog",
                "Test Blocked",
                "Accepted for Implementation",
                "Implementation Review",
                "In Analysis",
                "Waiting",
                "Provide Documentation",
                "In Progress",
            ]
        ]
        .sum(axis=1)
        .round(1)
    )
    extracted_issues["Total excluding Blocked/Planned"] = (
        extracted_issues[
            [
                "Backlog",
                "Accepted for Implementation",
                "Implementation Review",
                "In Analysis",
                "Waiting",
                "Provide Documentation",
                "In Progress",
            ]
        ]
        .sum(axis=1)
        .round(1)
    )
    extracted_issues["Percentage time in Deffect Discussion"] = (
        extracted_issues["Implementation Review"]
        / extracted_issues["Total excluding Blocked/Planned"]
    ).round(2)

    extracted_issues["DailyCommentCheck"] = extracted_issues.apply(
        lambda r: (
            check_daily_comments(
                [
                    datetime.datetime.strptime(d[:16], "%Y-%m-%dT%H:%M")
                    for d in r["comments_dates"]
                ],
                datetime.datetime.strptime(
                    r["sprints_startDate"][:16], "%Y-%m-%dT%H:%M"
                ),
                r["end date"],
            )
            if len(r["sprints_startDate"]) > 14
            else None
        ),
        axis=1,
    )
    extracted_issues["Test-Bug Tickets created"] = None

    extracted_issues["TestType"] = extracted_issues["summary"].map(extract_testtype)

    extracted_issues["test iteration"] = extracted_issues["labels"].map(
        extract_test_iteration
    )

    extracted_issues["test system"] = extracted_issues["Technology"].map(
        extract_test_system
    )

    extracted_issues["Tech-Cluster"] = extracted_issues["components"].map(transform_components)

    extracted_issues["Custom field (Epic Link)"] = extracted_issues["epic_link"].map(
        transform_epic_link
    )

    extracted_issues["Solution Train"] = extracted_issues["labels"].map(
        extract_solutiontrain
    )

    mask_Erstdurchdringung = (extracted_issues["resolution_date"].notna() & (extracted_issues["TestType"] == "FT")
                              & ~extracted_issues["status"].isin(['Cancelled', 'Test results not ok']))

    extracted_issues["Erstdurchdringung"] = None
    extracted_issues["Cluster"] = extracted_issues["Cluster"].fillna("")
    extracted_issues["Solution Train"] = extracted_issues["Solution Train"].fillna("")
    extracted_issues.loc[mask_Erstdurchdringung, "Erstdurchdringung"] = (
        extracted_issues.loc[mask_Erstdurchdringung]
        .groupby(["summary", "Cluster", "Solution Train"])["key"]
        .rank(method="dense", ascending=True)
    )
    extracted_issues.loc[mask_Erstdurchdringung, "Erstdurchdringung"] = (
        extracted_issues.loc[mask_Erstdurchdringung, "Erstdurchdringung"].map(
            lambda x: "x" if x == 1 else "o" if x > 1 else None
        )
    )

    extracted_issues["Current teststatus"] = extracted_issues["status"].map(
        treansfrom_status
    )

    extracted_issues["created [year/week]"] = extracted_issues["created"].map(
        lambda d: d.strftime("%Y/%V")
    )

    extracted_issues["resolved [year/week]"] = extracted_issues["resolution_date"].map(
        lambda d: (
            datetime.datetime.strptime(d[:10], "%Y-%m-%d").strftime("%Y/%V")
            if d
            else None
        )
    )
    extracted_issues["Test results FEA"] = extracted_issues["description"].map(
        lambda s: extract_betweendelimiters(
            s,
            "||Total amount of TCs||iO||niO||offen||Testblocker||Geblockt||Testfall Problem||Testinfrastruktur Problem||Durchführung abgebrochen||",
            "|",
            0,
            9,
        )
    )
    extracted_issues["Test results CB"] = extracted_issues["description"].map(
        lambda s: extract_betweendelimiters(
            s,
            "||Total amount of TCs||passed||failed||blocked||not applicable||not run yet||",
            "|",
            0,
            6,
        )
    )
    extracted_issues["Test results Raw"] = extracted_issues["description"].map(
        lambda s: extract_betweendelimiters(
            s, "||Total amount of TCs||iO||niO||offen||nicht geplant||", "|", 0, 5
        )
    )
    extracted_issues["Link to filled FEA"] = extracted_issues["description"].map(
        lambda s: extract_betweendelimiters(s, "Link to filled FEA+*", "*", 0, 0)
    )
    extracted_issues["Link to Raw Data"] = extracted_issues["description"].map(
        lambda s: extract_betweendelimiters(s, "Link to Raw Data+*", "*", 0, 0)
    )
    extracted_issues["Link to filled Codebeamer Excel"] = extracted_issues[
        "description"
    ].map(
        lambda s: extract_betweendelimiters(
            s, "Link to filled Codebeamer Excel+*", "*", 0, 0
        )
    )
    fea_cols = [
        "Test results FEA.1",
        "Number of TCs FEA.2",
        "io FEA.3",
        "nio FEA.4",
        "offen FEA.5",
        "Testblocker FEA.6",
        "Geblockt FEA.7",
        "Testfallproblem FEA.8",
        "Testinfrastruktur FEA.9",
        "abgebrochen FEA.10",
    ]
    raw_cols = [
        "Test results Raw.1",
        "Number of TCs Raw.2",
        "io Raw.3",
        "nio Raw.4",
        "offen Raw.5",
        "nicht geplant Raw.6",
    ]
    cb_cols = [
        "Test results CB.1",
        "Number of TCs CB.2",
        "passed CB.3",
        "failed CB.4",
        "blocked CB.5",
        "not applicable CB.6",
        "not run yet CB.7",
    ]
    extracted_issues = pd.concat(
        [
            extracted_issues,
            split_series(extracted_issues["Test results FEA"], "|", 10, fea_cols),
        ],
        axis=1,
    )
    extracted_issues = pd.concat(
        [
            extracted_issues,
            split_series(extracted_issues["Test results Raw"], "|", 6, raw_cols),
        ],
        axis=1,
    )

    extracted_issues = pd.concat(
        [
            extracted_issues,
            split_series(extracted_issues["Test results CB"], "|", 7, cb_cols),
        ],
        axis=1,
    )
    to_replace = """\<type here\>\+\*|Please write a detailed summary for the occurred problems after the hashtag summary\.|Please provide confluence link\(s\) to the documentation where you document your new findings / insights for the team \(e\. g\. new ECU configuration\, coding\)\.|\<enter Link\(s\) to Confluence here\>\+\*|\*\(x\) \+|\"\*\+\"\,"""
    extracted_issues["#Problems"] = (
        extracted_issues["description"]
        .map(lambda s: extract_betweendelimiters(s, "#Problems:", "#Summary", 0, 0))
        .str.replace(to_replace, "", regex=True)
        .str.strip()
    )
    extracted_issues["#Summary"] = (
        extracted_issues["description"]
        .map(lambda s: extract_betweendelimiters(s, "#Summary:", "#Links:", 0, 0))
        .str.replace(to_replace, "", regex=True)
        .str.strip()
    )
    extracted_issues["#Links"] = (
        extracted_issues["description"]
        .map(lambda s: extract_betweendelimiters(s, "#Links:", "", 0, 0))
        .str.replace(to_replace, "", regex=True)
        .str.strip()
    )
    extracted_issues["KPMs created list"] = extracted_issues["New KPM Tickets"].map(
        extract_kpm_extracted_list
    )
    extracted_issues["KPMs created count"] = extracted_issues["KPMs created list"].map(
        len
    )
    extracted_issues["KPMs verification list"] = extracted_issues["KPM-Tickets to test"].map(
        extract_kpm_verifictaion_list
    )
    extracted_issues["KPMs verification statuses"] = extracted_issues[
        "KPM-Tickets to test"
    ].map(extract_kpm_verifictaion_statuses)
    extracted_issues[
        "KPMs verification status count passed|failed|blocked|not tested"
    ] = extracted_issues["KPMs verification statuses"].map(
        lambda l: ",".join(
            [
                str(l.count("passed") + l.count("pass")),
                str(l.count("failed") + l.count("fail")),
                str(l.count("blocked")),
                str(l.count("not tested")),
            ]
        )
    )
    extracted_issues["passed"] = extracted_issues.apply(calculate_passed, axis=1)
    extracted_issues["failed"] = extracted_issues.apply(calculate_failed, axis=1)
    extracted_issues["blocked"] = extracted_issues.apply(calculate_blocked, axis=1)
    extracted_issues["not_applicable"] = extracted_issues.apply(
        calculate_not_applicable, axis=1
    )
    extracted_issues["not run yet"] = extracted_issues.apply(
        calculate_not_run_yet, axis=1
    )
    extracted_issues["Total applicable TCs"] = (
        extracted_issues["passed"].fillna(0)
        + extracted_issues["failed"].fillna(0)
        + extracted_issues["blocked"].fillna(0)
        + extracted_issues["not run yet"].fillna(0)
    )
    extracted_issues["Total TCs"] = (
        extracted_issues["passed"].fillna(0)
        + extracted_issues["failed"].fillna(0)
        + extracted_issues["blocked"].fillna(0)
        + extracted_issues["not run yet"].fillna(0)
        + extracted_issues["not_applicable"].fillna(0)
    )
    extracted_issues["Testcoverage (passed+failed)/ applicable"] = (
        extracted_issues.apply(
            lambda r: (
                (nan_fill(r["passed"])
                 + nan_fill(r["failed"])) / float(r["Total applicable TCs"])
                if r["Total applicable TCs"] > 0
                else 0
            ),
            axis=1,
        ).round(2)
    )

    extracted_issues["Results table filled"] = extracted_issues.apply(
        lambda r: (
            "-"
            if r["status"] != "Test results ok"
            else "x" if r["Total applicable TCs"] > 0 else "o"
        ),
        axis=1,
    )
    extracted_issues["Logfile available"] = extracted_issues.apply(
        lambda r: (
            "-"
            if r["status"] != "Test results ok"
            else (
                "x"
                if "volkswagengroup.sharepoint.com" in r["Link to Raw Data"]
                else "o"
            )
        ),
        axis=1,
    )

    extracted_issues["Jira ticket correct filled"] = extracted_issues.apply(
        lambda r: (
            "-"
            if r["status"] != "Test results ok"
            else (
                "x"
                if (
                    r["Results table filled"] == "x"
                    and r["Logfile available"] == "x"
                    and r["#Problems"]
                    and r["#Summary"]
                )
                else "o"
            )
        ),
        axis=1,
    )
    extracted_issues["Codebeamer Excels/FEAs available"] = extracted_issues.apply(
        lambda r: (
            "-"
            if r["status"] != "Test results ok"
            else (
                "x"
                if "volkswagengroup.sharepoint.com" in r["Link to filled FEA"]
                and "volkswagengroup.sharepoint.com"
                in r["Link to filled Codebeamer Excel"]
                else "o"
            )
        ),
        axis=1,
    )
    extracted_issues["KPMs finished"] = extracted_issues.apply(
        lambda r: (
            "-"
            if r["status"] != "Test results ok"
            else (
                "x"
                if r["Acceptance Criterias name"]
                or "false" not in r["Acceptance Criterias checks"]
                else "o"
            )
        ),
        axis=1,
    )
    extracted_issues["Percentage of not aborted / executed TCs"] = (
        extracted_issues.apply(
            lambda r: (
                (nan_fill(r["passed"])
                 + nan_fill(r["failed"])
                 + nan_fill(r["blocked"])) / float(r["Total TCs"])
                if r["Total TCs"] > 0
                else 0
            ),
            axis=1,
        ).round(2)
    )
    extracted_issues["Percentage of passed applicable TCs"] = extracted_issues.apply(
        lambda r: (
            nan_fill(r["passed"])
            / (
                nan_fill(r["passed"])
                + nan_fill(r["failed"])
                + nan_fill(r["not_applicable"])
                + nan_fill(r["not run yet"])
            )
            if nan_fill(r["passed"])
            + nan_fill(r["failed"])
            + nan_fill(r["not_applicable"])
            + nan_fill(r["not run yet"])
            > 0
            else 0
        ),
        axis=1,
    ).round(2)
    extracted_issues["Duration current Assignee_nw"] = extracted_issues.apply(
        lambda r: nb_w_days(r["end date"].date(), r["Current assignee date"].date()),
        axis=1,
    )

    integrity_criteria_df = extracted_issues[INITIAL_COLUMNS].copy()
    integrity_criteria_df.columns = TARGET_COLUMNS
    return integrity_criteria_df
