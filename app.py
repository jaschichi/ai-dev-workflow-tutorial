"""ShopSmart Sales Dashboard — Streamlit entry point."""

import streamlit as st

from data import generate_data, kpi_metrics

st.set_page_config(page_title="ShopSmart Dashboard", layout="wide")

df = generate_data()
metrics = kpi_metrics(df)

st.title("ShopSmart Sales Dashboard")
st.caption("E-commerce performance overview — 2024")

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${metrics['total_sales']:,.0f}")
col2.metric("Total Orders", metrics["total_orders"])
