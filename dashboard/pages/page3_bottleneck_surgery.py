"""
Dashboard Page 3 — Bottlenecks & Capacity Strain (Sarthak) + Surgery Workload (Aarthi — pending)
"""

import dash
from dash import html

dash.register_page(__name__, path="/page3", name="Page 3: Bottlenecks & Surgery")

layout = html.Div(
    [
        html.H3("Bottlenecks & Capacity Strain"),
        html.Iframe(
            src="/assets/reports/bottleneck_capacity.html",
            style={"width": "100%", "height": "1600px", "border": "none"},
        ),
        html.Hr(),
        html.H3("Surgery Workload"),
        html.Div(
            "Pending — Aarthi's visualization is in progress and expected tonight. "
            "Once received, drop the exported HTML into dashboard/assets/reports/ "
            "as 'surgery_workload.html' and replace this placeholder with the same "
            "Iframe pattern used above.",
            style={
                "padding": "20px",
                "background": "#fff8e1",
                "border": "1px dashed #d4a017",
                "borderRadius": "8px",
                "color": "#665200",
            },
        ),
    ],
    style={"padding": "24px"},
)
