from datetime import datetime
import os
import shutil
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import PatternFill


# Auto column width
def auto_adjust_columns(ws):
    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter

        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))

        ws.column_dimensions[col_letter].width = max_length + 3

# Style headers
def style_headers(ws):
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

# Add bar chart
def add_bar_chart(ws, title, data_col, category_col, position):
    chart = BarChart()
    chart.title = title

    data = Reference(ws, min_col=data_col, min_row=1, max_row=ws.max_row)
    cats = Reference(ws, min_col=category_col, min_row=2, max_row=ws.max_row)

    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)

    ws.add_chart(chart, position)

# Main Report Function
def generate_excel_report(kpis, analysis, anomalies, insights):
    # Create reports folder if not exists
    os.makedirs("reports", exist_ok=True)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    file_path = f"reports/financial_report_{timestamp}.xlsx"

    # Latest file
    latest_path = "reports/latest_report.xlsx"

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:

        # KPIs Sheet
        pd.DataFrame([kpis]).to_excel(writer, sheet_name="KPIs", index=False)

        # Monthly
        analysis["monthly"].to_excel(writer, sheet_name="Monthly", index=False)

        # Category
        analysis["category"].to_excel(writer, sheet_name="Category", index=False)

        # Region
        analysis["region"].to_excel(writer, sheet_name="Region", index=False)

        # Anomalies
        anomalies.to_excel(writer, sheet_name="Anomalies", index=False)

        # Insights
        pd.DataFrame({"Insights": insights}).to_excel(
            writer, sheet_name="Insights", index=False
        )

    # Post-formatting
    wb = load_workbook(file_path)

    # Apply formatting + charts
    for sheet in wb.sheetnames:
        ws = wb[sheet]

        auto_adjust_columns(ws)
        style_headers(ws)
    
    # Highlight anomalies
    red_fill = PatternFill(start_color="FF9999", end_color="FF9999", fill_type="solid")

    ws = wb["Anomalies"]
    for row in ws.iter_rows(min_row=2):
        expense = row[3].value  # adjust column index if needed
        if expense and expense > 2000:
            for cell in row:
                cell.fill = red_fill

    # ADD CHARTS

    # Monthly Chart
    ws = wb["Monthly"]
    add_bar_chart(ws, "Monthly Revenue", data_col=3, category_col=2, position="H2")

    # Category Chart
    ws = wb["Category"]
    add_bar_chart(ws, "Expense by Category", data_col=3, category_col=1, position="H2")

    # Region Chart
    ws = wb["Region"]
    add_bar_chart(ws, "Profit by Region", data_col=4, category_col=1, position="H2")

    wb.save(file_path)

    # Save latest version
    shutil.copy(file_path, latest_path)

    print(f"[INFO] Report saved: {file_path}")
    print("[INFO] Latest report updated")