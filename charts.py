"""Plotly figure builders for the ShopSmart sales dashboard."""

import plotly.graph_objects as go


def sales_trend_chart(monthly_series):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly_series.index.tolist(),
        y=monthly_series.values.tolist(),
        mode="lines+markers",
        hovertemplate="$%{y:,.0f}<extra></extra>",
    ))
    fig.update_layout(
        title="Monthly Sales Trend",
        xaxis_title="Month",
        yaxis_title="Revenue ($)",
        template="plotly_dark",
    )
    return fig


def category_chart(category_series):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=category_series.index.tolist(),
        y=category_series.values.tolist(),
        hovertemplate="$%{y:,.0f}<extra></extra>",
    ))
    fig.update_layout(
        title="Sales by Category",
        xaxis_title="Category",
        yaxis_title="Revenue ($)",
        template="plotly_dark",
    )
    return fig


def region_chart(region_series):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=region_series.index.tolist(),
        y=region_series.values.tolist(),
        hovertemplate="$%{y:,.0f}<extra></extra>",
    ))
    fig.update_layout(
        title="Sales by Region",
        xaxis_title="Region",
        yaxis_title="Revenue ($)",
        template="plotly_dark",
    )
    return fig
