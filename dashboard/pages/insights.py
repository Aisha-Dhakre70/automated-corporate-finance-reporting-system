import streamlit as st
import pandas as pd
import os
from utils.helper import apply_style

apply_style()

REPORT_PATH = "reports/latest_report.xlsx"

def show_insights():
    st.title("📌 Insights")

    if os.path.exists(REPORT_PATH):
        try:
            insights_df = pd.read_excel(REPORT_PATH, sheet_name="Insights")

            for i in insights_df["Insights"]:
                st.write("•", i)

        except:
            st.warning("Insights not found in report.")
    else:
        st.info("No report available yet.")