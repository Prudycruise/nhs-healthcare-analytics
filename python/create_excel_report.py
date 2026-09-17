import pandas as pd
from pathlib import Path

input_file = Path("data/cleaned/AE_attendances_cleaned.csv")
output_file = Path("excel/NHS_AE_Analysis.xlsx")

df = pd.read_csv(input_file, parse_dates=["date"])

# ---------- Summary tables ----------

monthly = (
    df.groupby("date", as_index=False)
      .agg({
          "Total attendances": "sum",
          "Percentage in 4 hours or less (all)": "mean"
      })
      .sort_values("date")
)

top_orgs = (
    df.groupby("Name", as_index=False)["Total attendances"]
      .sum()
      .sort_values("Total attendances", ascending=False)
      .head(10)
)

department_types = pd.DataFrame({
    "Department Type": [
        "Type 1 - Major A&E",
        "Type 2 - Single Specialty",
        "Type 3 - Other A&E / Minor Injury Unit"
    ],
    "Total Attendances": [
        df["Type 1 Departments - Major A&E"].sum(),
        df["Type 2 Departments - Single Specialty"].sum(),
        df["Type 3 Departments - Other A&E/Minor Injury Unit"].sum()
    ]
})

long_waits = (
    df.groupby("Name", as_index=False)[
        "Number of patients spending >12 hours from decision to admit to admission"
    ]
    .sum()
    .sort_values(
        "Number of patients spending >12 hours from decision to admit to admission",
        ascending=False
    )
    .head(10)
)

# ---------- Excel workbook ----------

with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    monthly.to_excel(writer, sheet_name="Monthly Trend", index=False)
    top_orgs.to_excel(writer, sheet_name="Top Organisations", index=False)
    department_types.to_excel(writer, sheet_name="Department Types", index=False)
    long_waits.to_excel(writer, sheet_name="12 Hour Waits", index=False)

    workbook = writer.book

    title_format = workbook.add_format({
        "bold": True,
        "font_size": 16,
        "font_color": "#FFFFFF",
        "bg_color": "#1F4E78"
    })

    header_format = workbook.add_format({
        "bold": True,
        "font_color": "#FFFFFF",
        "bg_color": "#4472C4",
        "border": 1
    })

    number_format = workbook.add_format({
        "num_format": "#,##0"
    })

    percent_format = workbook.add_format({
        "num_format": "0.0"
    })

    # Cleaned data
    ws = writer.sheets["Cleaned Data"]
    ws.freeze_panes(1, 0)
    ws.autofilter(0, 0, len(df), len(df.columns) - 1)
    ws.set_column(0, 0, 12)
    ws.set_column(1, 1, 48)
    ws.set_column(2, len(df.columns) - 1, 20)

    # Monthly trend
    ws = writer.sheets["Monthly Trend"]
    ws.freeze_panes(1, 0)
    ws.set_column("A:A", 14)
    ws.set_column("B:B", 20, number_format)
    ws.set_column("C:C", 25, percent_format)

    chart = workbook.add_chart({"type": "line"})
    chart.add_series({
        "name": "Total Attendances",
        "categories": ["Monthly Trend", 1, 0, len(monthly), 0],
        "values": ["Monthly Trend", 1, 1, len(monthly), 1],
    })
    chart.set_title({"name": "Total A&E Attendance Over Time"})
    chart.set_x_axis({"name": "Date"})
    chart.set_y_axis({"name": "Attendances", "num_format": "#,##0"})
    chart.set_legend({"none": True})
    ws.insert_chart("E2", chart, {"x_scale": 1.5, "y_scale": 1.4})

    # Top organisations
    ws = writer.sheets["Top Organisations"]
    ws.set_column("A:A", 55)
    ws.set_column("B:B", 20, number_format)

    chart = workbook.add_chart({"type": "bar"})
    chart.add_series({
        "name": "Total Attendances",
        "categories": ["Top Organisations", 1, 0, len(top_orgs), 0],
        "values": ["Top Organisations", 1, 1, len(top_orgs), 1],
    })
    chart.set_title({"name": "Top 10 NHS Organisations by A&E Attendance"})
    chart.set_legend({"none": True})
    ws.insert_chart("D2", chart, {"x_scale": 1.4, "y_scale": 1.5})

    # Department types
    ws = writer.sheets["Department Types"]
    ws.set_column("A:A", 38)
    ws.set_column("B:B", 22, number_format)

    chart = workbook.add_chart({"type": "column"})
    chart.add_series({
        "name": "Total Attendances",
        "categories": ["Department Types", 1, 0, len(department_types), 0],
        "values": ["Department Types", 1, 1, len(department_types), 1],
    })
    chart.set_title({"name": "Attendance by A&E Department Type"})
    chart.set_legend({"none": True})
    ws.insert_chart("D2", chart)

    # 12-hour waits
    ws = writer.sheets["12 Hour Waits"]
    ws.set_column("A:A", 55)
    ws.set_column("B:B", 25, number_format)

    chart = workbook.add_chart({"type": "bar"})
    chart.add_series({
        "name": "Patients >12 hours",
        "categories": ["12 Hour Waits", 1, 0, len(long_waits), 0],
        "values": ["12 Hour Waits", 1, 1, len(long_waits), 1],
    })
    chart.set_title({"name": "Organisations with Highest >12 Hour Waits"})
    chart.set_legend({"none": True})
    ws.insert_chart("D2", chart, {"x_scale": 1.4, "y_scale": 1.5})

    # Style headers on every sheet
    for sheet_name, dataframe in [
        ("Cleaned Data", df),
        ("Monthly Trend", monthly),
        ("Top Organisations", top_orgs),
        ("Department Types", department_types),
        ("12 Hour Waits", long_waits)
    ]:
        ws = writer.sheets[sheet_name]

        for col_num, value in enumerate(dataframe.columns):
            ws.write(0, col_num, value, header_format)

print(f"Workbook created: {output_file}")