"""
Admission Trends — Visualization component (Member 2 / Nafisa)
Registered as part of Page 1 alongside Tanvi's Department-wise Patient Load.
"""

import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html, Input, Output, callback

# ---------------------------------------------------------------------------
# 1. Load and prep data
# ---------------------------------------------------------------------------
df = pd.read_csv("data/processed/admissions_clean.csv")
df["Admission_Date"] = pd.to_datetime(df["Admission_Date"], errors="coerce")
df["Admission_Month_Year"] = df["Admission_Date"].dt.to_period("M").astype(str)

monthly_admissions = (
    df.groupby("Admission_Month_Year")["Admission_ID"]
    .nunique()
    .reset_index(name="Admission_Count")
    .sort_values("Admission_Month_Year")
)
monthly_admissions["Admission_Month_Year"] = pd.to_datetime(
    monthly_admissions["Admission_Month_Year"], format="%Y-%m"
)

# ---------------------------------------------------------------------------
# 2. KPIs
# ---------------------------------------------------------------------------
total_admissions = int(df["Admission_ID"].nunique())
avg_per_month = round(monthly_admissions["Admission_Count"].mean(), 1)
peak_row = monthly_admissions.loc[monthly_admissions["Admission_Count"].idxmax()]
low_row = monthly_admissions.loc[monthly_admissions["Admission_Count"].idxmin()]


def make_figure(filtered_df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=filtered_df["Admission_Month_Year"],
            y=filtered_df["Admission_Count"],
            mode="lines+markers",
            fill="tozeroy",
            line=dict(width=3),
            name="Admissions",
            hovertemplate="%{x|%b %Y}<br>Admissions: %{y}<extra></extra>",
        )
    )
    fig.update_layout(
        title="Monthly Admission Trend",
        xaxis_title="Month",
        yaxis_title="Number of Admissions",
        template="plotly_white",
        margin=dict(l=40, r=20, t=50, b=40),
    )
    return fig


def kpi_card(label: str, value) -> html.Div:
    return html.Div(
        [
            html.Div(label, style={"fontSize": "13px", "color": "#666"}),
            html.Div(str(value), style={"fontSize": "26px", "fontWeight": "700"}),
        ],
        style={
            "padding": "16px",
            "borderRadius": "10px",
            "background": "#f5f5f7",
            "textAlign": "center",
            "minWidth": "150px",
        },
    )


kpi_row = html.Div(
    [
        kpi_card("Total Admissions", f"{total_admissions:,}"),
        kpi_card("Avg / Month", avg_per_month),
        kpi_card(
            "Peak Month",
            f"{peak_row['Admission_Month_Year'].strftime('%b %Y')} ({int(peak_row['Admission_Count'])})",
        ),
        kpi_card(
            "Lowest Month",
            f"{low_row['Admission_Month_Year'].strftime('%b %Y')} ({int(low_row['Admission_Count'])})",
        ),
    ],
    style={"display": "flex", "gap": "16px", "marginBottom": "20px", "flexWrap": "wrap"},
)

range_slider = dcc.RangeSlider(
    id="admission-month-range",  # namespaced ID — unique across the whole app
    min=0,
    max=len(monthly_admissions) - 1,
    step=1,
    value=[0, len(monthly_admissions) - 1],
    marks={i: d.strftime("%b'%y") for i, d in enumerate(monthly_admissions["Admission_Month_Year"])},
)

# ---------------------------------------------------------------------------
# Exported layout piece — imported and placed into pages/page1_patient_flow.py
# ---------------------------------------------------------------------------
admissions_section = html.Div(
    [
        html.H3("Admission Trends"),
        kpi_row,
        html.Div(range_slider, style={"marginBottom": "24px", "padding": "0 12px"}),
        dcc.Graph(id="admission-chart", figure=make_figure(monthly_admissions)),
    ],
    style={"marginBottom": "40px"},
)


@callback(Output("admission-chart", "figure"), Input("admission-month-range", "value"))
def update_admission_chart(rng):
    sliced = monthly_admissions.iloc[rng[0] : rng[1] + 1]
    return make_figure(sliced)
