#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ============================================================
# SURGERY WORKLOAD DASHBOARD
# ============================================================

import pandas as pd
import plotly.graph_objects as go
from IPython.display import display, HTML

# ------------------------------------------------------------
# 1. LOAD SURGERY WORKLOAD ANALYSIS
# ------------------------------------------------------------

file_path = "Surgery_Workload.xlsx"

surgery_type = pd.read_excel(
    file_path,
    sheet_name="Surgery_Type_Analysis"
)

quarterly = pd.read_excel(
    file_path,
    sheet_name="Quarterly_Workload"
)

outcome = pd.read_excel(
    file_path,
    sheet_name="Outcome_Analysis"
)

recovery = pd.read_excel(
    file_path,
    sheet_name="Recovery_Analysis"
)

overall = pd.read_excel(
    file_path,
    sheet_name="Overall_KPIs"
)


# ------------------------------------------------------------
# 2. GET KPI VALUES
# ------------------------------------------------------------

kpi = dict(
    zip(
        overall.iloc[:, 0],
        overall.iloc[:, 1]
    )
)

total_surgeries = kpi["Total Surgeries"]

success_rate = kpi["Surgery Success Rate (%)"]

avg_duration = kpi["Average Surgery Duration (Minutes)"]

avg_cost = kpi["Average Surgery Cost"]

avg_recovery = kpi["Average Recovery Days"]


# ------------------------------------------------------------
# 3. KPI CARDS
# ------------------------------------------------------------

display(HTML(f"""

<h1 style="text-align:center;">
Surgery Workload Dashboard
</h1>

<p style="text-align:center;color:#666;">
Medical Operations Intelligence Dashboard
</p>

<div style="
display:flex;
gap:15px;
flex-wrap:wrap;
margin:25px 0;
">

<div style="
padding:20px;
background:#f5f5f7;
border-radius:10px;
text-align:center;
min-width:170px;
">
<div>Total Surgeries</div>
<h2>{int(total_surgeries):,}</h2>
</div>

<div style="
padding:20px;
background:#f5f5f7;
border-radius:10px;
text-align:center;
min-width:170px;
">
<div>Success Rate</div>
<h2>{success_rate:.2f}%</h2>
</div>

<div style="
padding:20px;
background:#f5f5f7;
border-radius:10px;
text-align:center;
min-width:170px;
">
<div>Avg Duration</div>
<h2>{avg_duration:.2f} min</h2>
</div>

<div style="
padding:20px;
background:#f5f5f7;
border-radius:10px;
text-align:center;
min-width:170px;
">
<div>Avg Cost</div>
<h2>₹{avg_cost:,.0f}</h2>
</div>

<div style="
padding:20px;
background:#f5f5f7;
border-radius:10px;
text-align:center;
min-width:170px;
">
<div>Avg Recovery</div>
<h2>{avg_recovery:.2f} days</h2>
</div>

</div>

"""))


# ------------------------------------------------------------
# 4. SURGERY TYPE CHART
# ------------------------------------------------------------

fig1 = go.Figure()

fig1.add_trace(
    go.Bar(
        x=surgery_type["Surgery_Type"],
        y=surgery_type["Total_Surgeries"],
        text=surgery_type["Total_Surgeries"],
        textposition="auto",
        hovertemplate=
        "<b>%{x}</b><br>"
        "Surgeries: %{y}"
        "<extra></extra>"
    )
)

fig1.update_layout(
    title="Surgery Workload by Surgery Type",
    xaxis_title="Surgery Type",
    yaxis_title="Number of Surgeries",
    template="plotly_white"
)

fig1.show()


# ------------------------------------------------------------
# 5. QUARTERLY WORKLOAD
# ------------------------------------------------------------

fig2 = go.Figure()

fig2.add_trace(
    go.Bar(
        x=quarterly["Surgery_Quarter"],
        y=quarterly["Total_Surgeries"],
        text=quarterly["Total_Surgeries"],
        textposition="auto",
        hovertemplate=
        "<b>Q%{x}</b><br>"
        "Surgeries: %{y}"
        "<extra></extra>"
    )
)

fig2.update_layout(
    title="Quarterly Surgery Workload",
    xaxis_title="Quarter",
    yaxis_title="Number of Surgeries",
    template="plotly_white"
)

fig2.show()


# ------------------------------------------------------------
# 6. SURGERY OUTCOME
# ------------------------------------------------------------

fig3 = go.Figure()

fig3.add_trace(
    go.Pie(
        labels=outcome["Outcome"],
        values=outcome["Total_Surgeries"],
        hole=0.4,
        textinfo="label+percent",
        hovertemplate=
        "<b>%{label}</b><br>"
        "Surgeries: %{value}"
        "<extra></extra>"
    )
)

fig3.update_layout(
    title="Surgery Outcomes",
    template="plotly_white"
)

fig3.show()


# ------------------------------------------------------------
# 7. RECOVERY ANALYSIS
# ------------------------------------------------------------

fig4 = go.Figure()

fig4.add_trace(
    go.Bar(
        x=recovery["Surgery_Type"],
        y=recovery["Average_Recovery_Days"],
        text=recovery["Average_Recovery_Days"].round(2),
        textposition="auto",
        hovertemplate=
        "<b>%{x}</b><br>"
        "Average Recovery: %{y:.2f} days"
        "<extra></extra>"
    )
)

fig4.update_layout(
    title="Average Recovery Days by Surgery Type",
    xaxis_title="Surgery Type",
    yaxis_title="Average Recovery Days",
    template="plotly_white"
)

fig4.show()


# ------------------------------------------------------------
# 8. AVERAGE DURATION
# ------------------------------------------------------------

fig5 = go.Figure()

fig5.add_trace(
    go.Bar(
        x=surgery_type["Surgery_Type"],
        y=surgery_type["Average_Duration_Minutes"],
        text=surgery_type["Average_Duration_Minutes"].round(2),
        textposition="auto",
        hovertemplate=
        "<b>%{x}</b><br>"
        "Average Duration: %{y:.2f} minutes"
        "<extra></extra>"
    )
)

fig5.update_layout(
    title="Average Surgery Duration by Surgery Type",
    xaxis_title="Surgery Type",
    yaxis_title="Average Duration (Minutes)",
    template="plotly_white"
)

fig5.show()


# In[ ]:




