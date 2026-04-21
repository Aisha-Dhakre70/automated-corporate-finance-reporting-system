import streamlit as st
import plotly.express as px

def show_overview():
    df = st.session_state.get("filtered_df")

    st.title("📊 Overview")

    # KPIs
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Revenue", f"{df['revenue'].sum():,.0f}")
    col2.metric("Expense", f"{df['expense'].sum():,.0f}")
    col3.metric("Profit", f"{df['net_profit'].sum():,.0f}")
    col4.metric("Margin", f"{(df['net_profit'].sum()/df['revenue'].sum())*100:.2f}%")

    # Trends
    st.subheader("📈 Trends")
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(px.line(df, x="date", y="revenue", color="company"), use_container_width=True)

    with col2:
        st.plotly_chart(px.line(df, x="date", y="net_profit", color="company"), use_container_width=True)

    # Breakdown
    st.subheader("📊 Breakdown")
    col1, col2 = st.columns(2)

    with col1:
        cat = df.groupby("category")["revenue"].sum().reset_index()
        st.plotly_chart(px.bar(cat, x="category", y="revenue"), use_container_width=True)

    with col2:
        reg = df.groupby("region")["net_profit"].sum().reset_index()
        st.plotly_chart(px.bar(reg, x="region", y="net_profit"), use_container_width=True)

    # Company
    st.subheader("🏢 Company Comparison")
    comp = df.groupby("company")["revenue"].sum().reset_index()
    st.plotly_chart(px.bar(comp, x="company", y="revenue"), use_container_width=True)

    # Anomalies
    st.subheader("⚠️ Anomalies")
    anomalies = df[df["net_profit"] < 0]

    if not anomalies.empty:
        st.dataframe(anomalies.head(20))
    else:
        st.info("No anomalies detected.")