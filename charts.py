"""Plotly figure builders for the ShopSmart sales dashboard."""

import plotly.graph_objects as go


def sales_trend_chart(monthly_series):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly_series.index.tolist(),
        y=monthly_series.values.tolist(),
        mode="lines+markers",
    ))
    fig.update_layout(
        title="Monthly Sales Trend",
        xaxis_title="Month",
        yaxis_title="Revenue ($)",
        template="plotly_dark",
    )
    return fig
