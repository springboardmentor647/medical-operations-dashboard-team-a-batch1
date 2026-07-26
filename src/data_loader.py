"""
data_loader.py
Loads all healthcare operational datasets (all REAL data, no synthetic files).
"""

import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_patients(path: Path = RAW_DATA_DIR / "patients.csv") -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["date_of_birth", "registration_date"])


def load_doctors(path: Path = RAW_DATA_DIR / "doctors.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def load_staff(path: Path = RAW_DATA_DIR / "staff.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def load_appointments(path: Path = RAW_DATA_DIR / "appointments.csv") -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["appointment_date"])


def load_treatments(path: Path = RAW_DATA_DIR / "treatments.csv") -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["treatment_date"])


def load_billing(path: Path = RAW_DATA_DIR / "billing.csv") -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["bill_date"])


def load_beds(path: Path = RAW_DATA_DIR / "beds.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def load_admissions(path: Path = RAW_DATA_DIR / "admissions_data.csv") -> pd.DataFrame:
    # admission_date is DD-MM-YYYY, unlike the other date columns in this project
    return pd.read_csv(path, parse_dates=["admission_date"], dayfirst=True)


def load_discharges(path: Path = RAW_DATA_DIR / "discharges_data.csv") -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["discharge_date"], dayfirst=True)


def load_all() -> dict:
    return {
        "patients": load_patients(),
        "doctors": load_doctors(),
        "staff": load_staff(),
        "appointments": load_appointments(),
        "treatments": load_treatments(),
        "billing": load_billing(),
        "beds": load_beds(),
        "admissions": load_admissions(),
        "discharges": load_discharges(),
    }


if __name__ == "__main__":
    data = load_all()
    for name, df in data.items():
        print(f"{name}: {df.shape} rows/cols")
        print(df.head(2), "\n")