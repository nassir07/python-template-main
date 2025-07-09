import pandas as pd
from openpyxl.utils import get_column_letter


def write_excel(df, file_path, sheet_name, formating, conditional_formating):
    writer = pd.ExcelWriter(file_path, engine="xlsxwriter")
    df.to_excel(
        writer,
        sheet_name=sheet_name,
        index=False,
        header=1,
    )
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    for cols, format in formating.items():
        workbook_format = workbook.add_format(format)
        for col in cols:
            col_posi = list(df.columns).index(col)
            # Apply the  format to the column.
            worksheet.set_column(col_posi, col_posi, None, workbook_format)
    start_row = 2
    end_row = len(df) + 1
    for cols, format_info in conditional_formating.items():
        workbook_format = workbook.add_format(format_info['format'])
        for col in cols:
            col_letter = get_column_letter(list(df.columns).index(col) + 1)
            worksheet.conditional_format(
                f"{col_letter}{start_row}:{col_letter}{end_row}",
                {
                    "type": format_info['type'],
                    "criteria": format_info['criteria'],
                    "value": format_info['value'],
                    "format": workbook_format,
                },
            )
    # Close the Pandas Excel writer and output the Excel file.
    writer.close()
