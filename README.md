# Medical Operations Dashboard — Team A, Batch 1

## Milestone 1: Healthcare Data Integration & Operational Analytics Layer

### Datasets
All data is real, provided by the team (Kaggle-sourced, extended with admissions/discharges/beds/staff):
- patients.csv, doctors.csv, staff.csv
- appointments.csv, treatments.csv, billing.csv
- admissions_data.csv, discharges_data.csv, beds.csv

### Notes on data
- `beds.csv` is a current snapshot of bed status, not a daily time series — occupancy rate reflects a point-in-time view, not a trend over time.
- `length_of_stay_days` comes directly from `discharges_data.csv`.
- `admission_date` uses DD-MM-YYYY format; other date fields use YYYY-MM-DD — handled in `data_loader.py`.

### Pipeline
- `src/data_loader.py` — loads all 9 raw datasets
- `src/preprocessing.py` — cleans and merges admissions + discharges + patients + doctors into `data/processed/admissions_integrated.csv`
- `src/kpi_metrics.py` — calculates KPIs:
  - Average Length of Stay
  - Bed occupancy rate by department
  - Admission volume by department
  - Admission type breakdown (Elective/Urgent/Emergency)
  - Staff-to-admission ratio by department
  - Against Medical Advice discharge rate (operational risk indicator)

### How to run
\`\`\`
cd src
python data_loader.py
python preprocessing.py
python kpi_metrics.py
\`\`\`
Or see `notebooks/01_data_cleaning_and_kpis.ipynb` for a walkthrough with output.