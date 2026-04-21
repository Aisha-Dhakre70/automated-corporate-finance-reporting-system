import streamlit as st
import pandas as pd
import os
import time
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Financial Dashboard", layout="wide")

DATA_PATH = "data/processed/cleaned_data.csv"
REFRESH_INTERVAL = 15

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# ---------------- AUTO REFRESH ----------------
def get_last_modified():
    if os.path.exists(DATA_PATH):
        return os.path.getmtime(DATA_PATH)
    return None

if "last_mod" not in st.session_state:
    st.session_state.last_mod = get_last_modified()

if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = time.time()

current_mod = get_last_modified()

if current_mod != st.session_state.last_mod:
    st.session_state.last_mod = current_mod
    st.toast("🔄 Data updated")
    st.rerun()

if time.time() - st.session_state.last_refresh > REFRESH_INTERVAL:
    st.session_state.last_refresh = time.time()
    st.rerun()

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 Navigation")

page = st.sidebar.radio("Go to", ["Overview", "Insights", "Reports"])

st.sidebar.markdown("## 🎛️ Filters")

company = st.sidebar.multiselect("Company", df["company"].unique(), default=df["company"].unique())
region = st.sidebar.multiselect("Region", df["region"].unique(), default=df["region"].unique())
category = st.sidebar.multiselect("Category", df["category"].unique(), default=df["category"].unique())

# Apply filters

min_date = df["date"].min()
max_date = df["date"].max()

# Preset options
date_option = st.sidebar.radio(
    "Select Date Range",
    ["All Time", "Last 7 Days", "Last 30 Days", "Last 90 Days", "Custom"],
    index=0
)

# Logic
if date_option == "All Time":
    start_date, end_date = min_date, max_date

elif date_option == "Last 7 Days":
    end_date = max_date
    start_date = end_date - pd.Timedelta(days=7)

elif date_option == "Last 30 Days":
    end_date = max_date
    start_date = end_date - pd.Timedelta(days=30)

elif date_option == "Last 90 Days":
    end_date = max_date
    start_date = end_date - pd.Timedelta(days=90)

elif date_option == "Custom":
    start_date, end_date = st.sidebar.slider(
        "Select Date Range",
        min_value=min_date.to_pydatetime(),
        max_value=max_date.to_pydatetime(),
        value=(min_date.to_pydatetime(), max_date.to_pydatetime())
    )

# Convert to pandas datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

df = df[
    (df["company"].isin(company)) &
    (df["region"].isin(region)) &
    (df["category"].isin(category)) &
    (df["date"] >= start_date) &
    (df["date"] <= end_date)
]

# Store globally
st.session_state["filtered_df"] = df

# Last updated
if current_mod:
    st.caption(f"🕒 Last update: {datetime.datetime.fromtimestamp(current_mod)}")

# ---------------- ROUTING ----------------
if page == "Overview":
    from dashboard.pages.overview import show_overview
    show_overview()

elif page == "Insights":
    from dashboard.pages.insights import show_insights
    show_insights()

elif page == "Reports":
    from dashboard.pages.reports import show_reports
    show_reports()