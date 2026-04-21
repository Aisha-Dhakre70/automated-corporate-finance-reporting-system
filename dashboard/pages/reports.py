import streamlit as st
import os
from utils.helper import apply_style

apply_style()

REPORT_PATH = "reports/latest_report.xlsx"

def show_reports():
    st.title("📄 Reports")

    if os.path.exists(REPORT_PATH):

        with open(REPORT_PATH, "rb") as f:
            st.download_button(
                label="📥 Download Latest Report",
                data=f,
                file_name="financial_report.xlsx"
            )

        st.success("Latest report available.")

    else:
        st.warning("No reports generated yet.")