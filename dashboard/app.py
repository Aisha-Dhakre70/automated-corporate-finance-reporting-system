import streamlit as st
import pandas as pd
import plotly.express as px
import os
import time
import datetime

# ---------------- CONFIG ----------------
DATA_PATH = "data/processed/processed_data.csv"
REFRESH_INTERVAL = 15  # seconds
st.set_page_config(page_title="Financial Dashboard", layout="wide")

# ---------------- HELPER FUN --------------
def get_data_last_modified():
    if os.path.exists(DATA_PATH):
        return os.path.getmtime(DATA_PATH)
    return None

# ----------------- SESSION STATE INITIALIZATION -----------------
if "data_last_modified" not in st.session_state:
    st.session_state.data_last_modified = get_data_last_modified()

if "last_refresh_time" not in st.session_state:
    st.session_state.last_refresh_time = time.time()

# ---------------- STYLING ----------------
st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}

.kpi-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    text-align: center;
    border: 1px solid #e5e7eb;
}

.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 30px;
    margin-bottom: 10px;
}

hr {
    border: none;
    height: 1px;
    background-color: #e6e9ef;
    margin: 25px 0;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
DATA_PATH = "data/processed/cleaned_data.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# --------------- DETECT DATA CHANGE ---------------
current_modified = get_data_last_modified()

if current_modified != st.session_state.data_last_modified:
    st.session_state.data_last_modified = current_modified
    st.toast("🔄 New data detected. Refreshing dashboard...")
    st.rerun()

# --------------- AUTO REFRESH -----------------
if time.time() - st.session_state.last_refresh_time > REFRESH_INTERVAL:
    st.session_state.last_refresh_time = time.time()
    st.rerun()

# ---------------- HEADER ----------------
st.title("📊 Financial Dashboard")
st.caption("Automated Corporate Financial Reporting System")

# --------------- UI LAST UPDATED ---------------
last_updated = get_data_last_modified()

if last_updated:
    st.caption(
        f"🕒 Last data update: {datetime.datetime.fromtimestamp(last_updated).strftime('%Y-%m-%d %H:%M:%S')}"
    )

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 🎛️ Filters")

company = st.sidebar.multiselect(
    "Company", df["company"].unique(), default=df["company"].unique()
)

region = st.sidebar.multiselect(
    "Region", df["region"].unique(), default=df["region"].unique()
)

category = st.sidebar.multiselect(
    "Category", df["category"].unique(), default=df["category"].unique()
)

date_range = st.sidebar.date_input(
    "Date Range", [df["date"].min(), df["date"].max()]
)

# Apply filters
df = df[
    (df["company"].isin(company)) &
    (df["region"].isin(region)) &
    (df["category"].isin(category)) &
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1]))
]

# ---------------- KPI FUNCTION ----------------
def kpi_card(title, value):
    st.markdown(f"""
    <div class="kpi-card">
        <h4 style="color:#6b7280; margin-bottom:10px;">{title}</h4>
        <h2 style="color:#111827;">{value}</h2>
    </div>
    """, unsafe_allow_html=True)

# ---------------- KPIs ----------------
col1, col2, col3, col4 = st.columns(4)

total_revenue = df["revenue"].sum()
total_expense = df["expense"].sum()
total_profit = df["net_profit"].sum()
margin = (total_profit / total_revenue * 100) if total_revenue != 0 else 0

with col1:
    kpi_card("💰 Revenue", f"{total_revenue:,.0f}")

with col2:
    kpi_card("📉 Expense", f"{total_expense:,.0f}")

with col3:
    kpi_card("📈 Profit", f"{total_profit:,.0f}")

with col4:
    kpi_card("📊 Margin", f"{margin:.2f}%")

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- COLORS ----------------
COLOR_MAIN = "#4F8BF9"
COLOR_SECOND = "#F95F62"

# ---------------- TRENDS ----------------
st.markdown('<div class="section-title">📈 Trends</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    fig = px.line(df, x="date", y="revenue")
    fig.update_traces(line=dict(color=COLOR_MAIN))
    fig.update_layout(template="plotly_white", margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.line(df, x="date", y="net_profit")
    fig.update_traces(line=dict(color=COLOR_SECOND))
    fig.update_layout(template="plotly_white", margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- BREAKDOWN ----------------
st.markdown('<div class="section-title">📊 Breakdown</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    cat = df.groupby("category")["revenue"].sum().reset_index()
    fig = px.bar(cat, x="category", y="revenue")
    fig.update_traces(marker_color=COLOR_MAIN)
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    reg = df.groupby("region")["net_profit"].sum().reset_index()
    fig = px.bar(reg, x="region", y="net_profit")
    fig.update_traces(marker_color=COLOR_SECOND)
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- COMPANY ----------------
st.markdown('<div class="section-title">🏢 Company Comparison</div>', unsafe_allow_html=True)

comp = df.groupby("company")["revenue"].sum().reset_index()
fig = px.bar(comp, x="company", y="revenue")
fig.update_traces(marker_color=COLOR_MAIN)
fig.update_layout(template="plotly_white")
st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- ANOMALIES ----------------
st.markdown('<div class="section-title">⚠️ Anomalies</div>', unsafe_allow_html=True)

anomalies = df[df["net_profit"] < 0]

def highlight_negative(val):
    if val < 0:
        return 'background-color: #ffcccc; color: #111827; font-weight: 500;'
    else:
        return 'color: #111827;'

if not anomalies.empty:
    st.dataframe(
        anomalies.style.applymap(highlight_negative, subset=["net_profit"])
    )
else:
    st.info("No anomalies detected.")

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- INSIGHTS ----------------
REPORT_PATH = "reports/latest_report.xlsx"

if os.path.exists(REPORT_PATH):
    try:
        insights_df = pd.read_excel(REPORT_PATH, sheet_name="Insights")

        st.markdown('<div class="section-title">📌 Insights</div>', unsafe_allow_html=True)

        for i in insights_df["Insights"]:
            st.write("•", i)

    except:
        st.warning("Insights sheet not found in report.")

# ---------------- DOWNLOAD REPORT ----------------
if os.path.exists(REPORT_PATH):
    with open(REPORT_PATH, "rb") as f:
        st.download_button(
            label="📥 Download Latest Excel Report",
            data=f,
            file_name="financial_report.xlsx"
        )