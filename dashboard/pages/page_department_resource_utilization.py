"""
Dashboard Page — Department-wise Resource Utilization (Member 5 analysis / Member 6 visualization)

Route left as a descriptive slug rather than a guessed page number
(page4/page5/...) since the other three Milestone-3 Type B members
(Bed Utilization, Workforce & Staffing, Benchmark & Capacity Gap) may
independently be choosing their own page numbers in parallel. Member 9
(Dashboard Integration Lead) can rename/renumber this route to fit the
final page order without touching the component itself.
"""

import dash
from dash import html

dash.register_page(
    __name__,
    path="/department-resource-utilization",
    name="Department-wise Resource Utilization",
)

layout = html.Div(
    [
        html.H3("Department-wise Resource Utilization"),
        html.P(
            "Which departments show the greatest resource strain, combining "
            "doctor workload and bed utilization?",
            style={"color": "#666"},
        ),
        html.Iframe(
            src="/assets/reports/department_resource_utilization.html",
            style={"width": "100%", "height": "3400px", "border": "none"},
        ),
    ],
    style={"padding": "24px"},
)
