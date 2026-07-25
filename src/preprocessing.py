"""
preprocessing.py
Cleans each dataset and builds the integrated admissions dataset
(admissions + discharges + patients + doctors), the leading dataset
for Milestone 1 KPIs.
"""

import pandas as pd
from pathlib import Path
from data_loader import load_all

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

KNOWN_ACRONYMS = {"Icu": "ICU"}


def fix_acronyms(series: pd.Series) -> pd.Series:
    return series.replace(KNOWN_ACRONYMS)


def clean_patients(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset="patient_id").dropna(subset=["patient_id"])


def clean_doctors(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="doctor_id").dropna(subset=["doctor_id"])
    df["hospital_branch"] = df["hospital_branch"].str.strip()
    df["specialization"] = df["specialization"].str.strip()
    return df


def clean_staff(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="staff_id").dropna(subset=["staff_id"])
    df["department"] = fix_acronyms(df["department"].str.strip().str.title())
    df["role"] = df["role"].str.strip().str.title()
    df["hospital_branch"] = df["hospital_branch"].str.strip()
    return df


def clean_beds(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="bed_id").dropna(subset=["bed_id"])
    df["department"] = fix_acronyms(df["department"].str.strip().str.title())
    df["status"] = df["status"].str.strip().str.title()
    df["hospital_branch"] = df["hospital_branch"].str.strip()
    return df


def clean_admissions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="admission_id").dropna(subset=["admission_id", "admission_date"])
    df["department"] = fix_acronyms(df["department"].str.strip().str.title())
    df["admission_type"] = df["admission_type"].str.strip().str.title()
    df["hospital_branch"] = df["hospital_branch"].str.strip()
    return df


def clean_discharges(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="discharge_id").dropna(subset=["discharge_id", "admission_id"])
    df["discharge_status"] = df["discharge_status"].str.strip().str.title()
    return df


def build_integrated_admissions_dataset(admissions, discharges, patients, doctors) -> pd.DataFrame:
    """One row per admission, enriched with discharge outcome, patient, and doctor info."""
    df = admissions.merge(discharges, on=["admission_id", "patient_id"], how="left")
    df = df.merge(
        patients[["patient_id", "gender", "insurance_provider"]], on="patient_id", how="left"
    )
    df = df.merge(
        doctors[["doctor_id", "specialization", "years_experience"]].rename(
            columns={"doctor_id": "attending_doctor_id"}
        ),
        on="attending_doctor_id", how="left"
    )
    return df


def run_pipeline():
    raw = load_all()

    patients = clean_patients(raw["patients"])
    doctors = clean_doctors(raw["doctors"])
    staff = clean_staff(raw["staff"])
    beds = clean_beds(raw["beds"])
    admissions = clean_admissions(raw["admissions"])
    discharges = clean_discharges(raw["discharges"])

    integrated = build_integrated_admissions_dataset(admissions, discharges, patients, doctors)

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    integrated.to_csv(PROCESSED_DATA_DIR / "admissions_integrated.csv", index=False)
    staff.to_csv(PROCESSED_DATA_DIR / "staff_clean.csv", index=False)
    beds.to_csv(PROCESSED_DATA_DIR / "beds_clean.csv", index=False)

    print("Pipeline complete. Processed files written to data/processed/")
    print(f"  admissions_integrated.csv -> {integrated.shape}")
    print(f"  staff_clean.csv           -> {staff.shape}")
    print(f"  beds_clean.csv            -> {beds.shape}")

    return integrated, staff, beds


if __name__ == "__main__":
    run_pipeline()