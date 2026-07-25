"""
kpi_metrics.py
Calculates operational KPIs from the fully real dataset:
admissions + discharges (integrated), staff, and beds.
"""

import pandas as pd


def average_length_of_stay(integrated_df: pd.DataFrame) -> float:
    return round(integrated_df["length_of_stay_days"].mean(), 2)


def bed_occupancy_rate(beds_df: pd.DataFrame) -> pd.DataFrame:
    """Snapshot bed occupancy % by department, based on current bed status."""
    summary = (
        beds_df.groupby(["department", "status"]).size().unstack(fill_value=0)
    )
    summary["total_beds"] = summary.sum(axis=1)
    if "Occupied" not in summary.columns:
        summary["Occupied"] = 0
    summary["occupancy_rate_pct"] = (summary["Occupied"] / summary["total_beds"] * 100).round(2)
    return summary.reset_index()[["department", "total_beds", "Occupied", "occupancy_rate_pct"]]


def admission_volume_by_department(integrated_df: pd.DataFrame) -> pd.DataFrame:
    """Avg admissions per day, per department -- patient flow / demand indicator."""
    daily = (
        integrated_df.groupby(["department", "admission_date"])
        .size()
        .groupby("department")
        .mean()
        .round(2)
    )
    return daily.reset_index(name="avg_admissions_per_day")


def admission_type_breakdown(integrated_df: pd.DataFrame) -> pd.DataFrame:
    """% breakdown of Elective / Urgent / Emergency admissions -- demand/risk signal."""
    counts = (integrated_df["admission_type"].value_counts(normalize=True) * 100).round(2)
    return counts.rename_axis("admission_type").reset_index(name="pct_of_admissions")


def staff_to_patient_ratio(staff_df: pd.DataFrame, integrated_df: pd.DataFrame) -> pd.DataFrame:
    staff_counts = staff_df.groupby("department").size().rename("staff_count")
    admission_counts = integrated_df.groupby("department").size().rename("admission_count")
    combined = pd.concat([staff_counts, admission_counts], axis=1).fillna(0)
    ratio = combined["staff_count"] / combined["admission_count"].replace(0, float("nan"))
    combined["staff_to_admission_ratio"] = ratio.round(3)
    return combined.reset_index().rename(columns={"index": "department"})


def discharge_outcome_risk_rate(integrated_df: pd.DataFrame) -> float:
    """% of discharges that were 'Against Medical Advice' -- operational risk indicator."""
    total = len(integrated_df)
    at_risk = (integrated_df["discharge_status"] == "Against Medical Advice").sum()
    return round((at_risk / total) * 100, 2) if total else 0.0


def generate_kpi_summary(integrated_df: pd.DataFrame, staff_df: pd.DataFrame, beds_df: pd.DataFrame) -> dict:
    return {
        "average_length_of_stay_days": average_length_of_stay(integrated_df),
        "bed_occupancy_rate_by_department": bed_occupancy_rate(beds_df),
        "admission_volume_by_department": admission_volume_by_department(integrated_df),
        "admission_type_breakdown_pct": admission_type_breakdown(integrated_df),
        "staff_to_admission_ratio_by_department": staff_to_patient_ratio(staff_df, integrated_df),
        "against_medical_advice_rate_pct": discharge_outcome_risk_rate(integrated_df),
    }


if __name__ == "__main__":
    from preprocessing import run_pipeline

    integrated_df, staff_df, beds_df = run_pipeline()
    summary = generate_kpi_summary(integrated_df, staff_df, beds_df)

    print("\n--- KPI SUMMARY ---")
    print(f"Average Length of Stay: {summary['average_length_of_stay_days']} days")
    print(f"Against Medical Advice Rate: {summary['against_medical_advice_rate_pct']}%")
    print("\nBed Occupancy Rate by Department:")
    print(summary["bed_occupancy_rate_by_department"])
    print("\nAvg Admissions/Day by Department:")
    print(summary["admission_volume_by_department"])
    print("\nAdmission Type Breakdown (%):")
    print(summary["admission_type_breakdown_pct"])
    print("\nStaff-to-Admission Ratio by Department:")
    print(summary["staff_to_admission_ratio_by_department"])