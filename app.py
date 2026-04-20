"""ShopSmart Sales Dashboard — Streamlit entry point."""

import streamlit as st

from charts import category_chart, region_chart, sales_trend_chart
from data import category_summary, generate_data, kpi_metrics, monthly_trend, region_summary

st.set_page_config(page_title="ShopSmart Dashboard", layout="wide")

df = generate_data()
metrics = kpi_metrics(df)

st.title("ShopSmart Sales Dashboard")
st.caption("E-commerce performance overview — 2024")

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${metrics['total_sales']:,.0f}")
col2.metric("Total Orders", metrics["total_orders"])

st.plotly_chart(sales_trend_chart(monthly_trend(df)), use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(category_chart(category_summary(df)), use_container_width=True)
with col4:
    st.plotly_chart(region_chart(region_summary(df)), use_container_width=True)
