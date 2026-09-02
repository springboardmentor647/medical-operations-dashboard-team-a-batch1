# ðŸ¥ Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics Group 1

## ðŸ“Œ Project Overview
The **Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics Group 1** is a healthcare analytics project developed as part of the **Infosys Springboard Internship**. The project focuses on collecting, preprocessing, integrating, and analyzing healthcare datasets to generate meaningful insights and support dashboard development.

### Objectives
* Collect healthcare datasets.
* Clean and preprocess the datasets.
* Integrate multiple datasets into a unified dataset.
* Generate Key Performance Indicators (KPIs).
* Perform trend analysis.
* Build a dashboard for healthcare insights.
* Maintain the project using GitHub.

### Technologies Used
* Python
* Pandas
* NumPy
* Jupyter Notebook
* Git
* GitHub

---

## ðŸ“‚ Project Structure
```
medical-operations-dashboard-team-a-batch1
â”‚
â”œâ”€â”€ data/
â”‚   â””â”€â”€ raw/
â”œâ”€â”€ notebooks/
â”œâ”€â”€ src/
â”œâ”€â”€ README.md
```

---

## ðŸ“Š Datasets Used
* admissions.csv
* billing.csv
* departments.csv
* doctors.csv
* lab_results.csv
* medications.csv
* patients.csv
* raw_surgeries.csv

---

## ðŸ”„ Project Workflow
1. Data Collection
2. Data Preprocessing
3. Data Integration
4. KPI Generation
5. Trend Analysis
6. Documentation & GitHub
7. Dashboard Development

---

## ðŸ‘¥ Team Members
| Team Member | Responsibility |
|-------------|----------------|
| Sowmitha | Data Collection, Documentation & GitHub |
| Tanvi Bhosale | Data Preprocessing (Patients Dataset) |
| Sarthak | Data Preprocessing (Lab & Billing Datasets) |
| Sirivalli Reddyvari | Data Preprocessing (Doctors Dataset) |
| Nafisa | Data Preprocessing (Departments & Admissions Datasets) |
| Divya Kumari | Data Integration |
| Rushikesh | Data Preprocessing (Surgery Dataset) |
| Indhumathi K | Data Preprocessing (Medications Dataset) |
| Deepika J | KPI Generation |
| Abhi | Trend Analysis |

---

## ðŸ‘¥ Team Milestone 1 Completed
* Data Collection
* Data Preprocessing
* Data Integration
* KPI Generation
* Trend Analysis
* GitHub Collaboration
* Documentation

### ðŸš€ Future Work
* Develop an interactive Power BI Dashboard.
* Create advanced healthcare visualizations.
* Enhance KPI reporting.
* Improve operational insights.

### ðŸ“œ License
This project was developed for educational purposes as part of the Infosys Springboard Internship.

---

## ** ---- Milestone 2 â€“ Patient Flow & Service Demand Intelligence -----**

### ðŸ“Œ 1. Project Overview
Milestone 2 focuses on transforming the cleaned healthcare datasets prepared during Milestone 1 into meaningful operational insights. The team performs Exploratory Data Analysis (EDA), KPI generation, trend analysis, visualization, and dashboard development to support healthcare operational decision-making.

### ðŸ” 2. Milestone 2 Objective
The main objective of Milestone 2 is to analyze patient flow and healthcare service demand and convert the results into interactive dashboard insights.

#### Objectives
* Analyze admission and discharge patterns.
* Analyze department-wise patient workload.
* Monitor treatment and service demand.
* Identify operational bottlenecks and capacity strain.
* Analyze surgery workload.
* Generate KPIs and trends.
* Develop visualizations for dashboard integration.

### ðŸ¤– 3. Business Questions
Milestone 2 is organized around six core business questions:
1. Admission Trends
2. Department-wise Patient Load
3. Patient Discharge & Flow
4. Treatment & Service Demand
5. Bottlenecks & Capacity Strain
6. Surgery Workload

*Each business question is handled by one Type A and one Type B team member.*

---

### ðŸ—’ï¸ 4. Task Division

| Business Question | Type A â€“ Analysis | Type B â€“ Visualization |
|---|---|---|
| Admission Trends | Divya | Nafisa |
| Department-wise Patient Load | Srivalli | Tanvi |
| Patient Discharge & Flow | Sowmitha | Keerthi |
| Treatment & Service Demand | Abhinay | Sarthak |
| Bottlenecks & Capacity Strain | Sarthak | Sarthak |
| Surgery Workload | Deepika | Aarthi / Divya |
| Dashboard Integration | Nafisa | â€” |
| Documentation | Sowmitha | â€” |

*Type A members perform EDA and KPI analysis, while Type B members convert the findings into visualizations and dashboard components.*

---

### ðŸ“‚ 5. Datasets Used

* **Admission Trends:** `admissions_clean.csv`
* **Department-wise Patient Load:** `admissions_clean.csv`, `departments_clean.csv`
* **Patient Discharge & Flow:** `admissions_clean.csv`
* **Treatment & Service Demand:** `lab_results_clean.csv`, `billing_clean.csv`
* **Bottlenecks & Capacity Strain:** `admissions_clean.csv`, `doctors_preprocessed.csv`, `departments_clean.csv`
* **Surgery Workload:** `surgeries_clean_fixed.csv`

---

### ðŸ“œ 6. Analysis Methodology
The Milestone 2 workflow follows:
`Data Loading â†’ Data Validation â†’ Exploratory Data Analysis â†’ KPI Generation â†’ Trend Analysis â†’ Findings â†’ Visualization â†’ Dashboard Integration`

Python and Pandas are used for data analysis and KPI generation.

---

### â¬‡ï¸ 7. Patient Discharge & Flow Analysis
For the Patient Discharge & Flow business question, the analysis uses:
* `Discharge_Date`
* `Status`
* `Length_of_Stay_Days`

The analysis focuses on the admission-to-discharge timeline and patient status transitions. Since no movement or transfer log is available, ward-to-ward patient movement is not analyzed.

#### ðŸ“Š KPIs Generated
* Total Patients
* Average Length of Stay
* Discharge Rate
* Patient Status Distribution
* Monthly Admissions
* Monthly Discharges
* Department-wise Admissions
* Department-wise Discharges
* Department-wise Discharge Rate

#### ðŸ”‘ Key Results
* **Total Patients:** 5,000
* **Average Length of Stay:** 5.52 days
* **Discharge Rate:** 24.28%
* **Critical Patients:** 1,279
* **Under Treatment:** 1,272
* **Recovered Patients:** 1,235
* **Discharged Patients:** 1,214
* **Highest Monthly Admissions:** July â€“ 524
* **Highest Monthly Discharges:** March â€“ 584
* **Highest Department Admissions:** D015 â€“ 335
* **Highest Department Discharge Rate:** D004 â€“ 30.32%

---

### ðŸ“ˆ 8. Visualization
The Type B members use the KPI outputs and findings from Type A analysis to create dashboard visualizations. Planned visualizations include:
* Admission trend charts
* Department-wise workload charts
* Patient status distribution
* Monthly admission and discharge trends
* Length of Stay analysis
* Treatment and service demand charts
* Bottleneck and capacity indicators
* Surgery workload visualizations

---

### âš™ï¸ 9. Tools & Technologies
* Python
* Pandas
* NumPy
* Matplotlib
* Plotly / Dash or Power BI
* Google Colab
* Git & GitHub

---

### ðŸ”„ 10. GitHub Workflow
The team uses GitHub for collaborative development and documentation:
`Clone Repository â†’ Create/Use Working Branch â†’ Perform Analysis â†’ Commit Changes â†’ Push Changes â†’ Review/Integrate â†’ Dashboard Assembly`

Work is pushed regularly so that dashboard integration can happen smoothly.

---

### âš ï¸ 11. Challenges & Solutions
* **Challenge 1: Different Business Questions**
  * *Solution:* Tasks were divided into six business questions with dedicated Type A and Type B members.
* **Challenge 2: Missing Patient Movement Data**
  * *Solution:* Patient flow was analyzed using admission-to-discharge timelines and status transitions since no transfer logs existed.
* **Challenge 3: Multiple Dataset Requirements**
  * *Solution:* Relevant datasets were mapped to each business question and joined where required.
* **Challenge 4: Dashboard Integration**
  * *Solution:* Type A members provide KPI numbers and findings to Type B members for visualization and dashboard integration.

---

### ðŸ“¦ 12. Milestone 2 Deliverables
* EDA and KPI analysis notebooks
* Business-question-specific findings
* KPI summary tables
* Visualization outputs
* Dashboard components
* GitHub updates
* README documentation
* Final integrated dashboard

#### ðŸš€ How to Run the Dashboard
1. Clone the repo and navigate to the project root
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Mac/Linux
   ```
3. Install dependencies:
   ```bash
   pip install dash plotly pandas
   ```
4. Run the app:
   ```bash
   python dashboard/app.py
   ```
5. Open http://localhost:8050 in your browser
6. Use the nav links at the top (Page 1, 2, 3) to view each business question's visualizations

#### Status
- Page 1: Admission Trends + Department-wise Patient Load âœ…
- Page 2: Patient Discharge & Flow + Treatment & Service Demand âœ…
- Page 3: Bottlenecks & Capacity Strain âœ…, Surgery Workload pending

---

### ðŸ”® 13. Future Work
* Complete dashboard integration.
* Improve interactive visualizations.
* Add advanced operational indicators.
* Validate all KPI outputs.
* Finalize documentation and presentation.
* Integrate all business-question outputs into the final dashboard.

---

### ðŸŽ¯ 14. Conclusion
Milestone 2 transforms the cleaned healthcare datasets from Milestone 1 into actionable operational intelligence. Through EDA, KPI generation, trend analysis, visualization, and dashboard integration, the project provides insights into patient flow, service demand, workload, operational bottlenecks, and surgery workload. The completed outputs will serve as the foundation for the final Medical Operations Intelligence Dashboard.

---

## ** ---- Milestone 3 â€“ Resource Utilization & Capacity Intelligence Module -----**

### ðŸ“Œ 1. Milestone 3 Overview & Objective
**Weeks 5-6 | Team of 10**

Milestone 3 focuses on **Resource Utilization & Capacity Intelligence** â€” developing healthcare resource intelligence dashboards and capacity monitoring capabilities covering bed utilization, workforce efficiency, department-wise resource distribution, and benchmark/capacity gap analysis.

---

### ðŸ“Š 2. Data Notes - Benchmark Gap Datasets (Resolved)

**Bed Capacity Gap (`data/raw/bed_capacity.csv`):**
* **Contents:** `department_id`, `department_name`, `Total_Beds` (one row per department)
* **Purpose:** Benchmark bed counts defined by the team to allow Bed Utilization (BQ 1) calculation.
* **Usage:** Joined against `admissions_clean.csv` on `department_id` to compute occupancy and available beds.

**Staff Capacity Gap (`data/raw/staff_capacity.csv`):**
* **Contents:** `department_id`, `department_name`, `Total_Staff` (one row per department)
* **Purpose:** Benchmark staff counts representing full healthcare staffing in proportion to bed capacity and patient-facing intensity.
* **Usage:** Joined against `doctors_preprocessed.csv` and `admissions_clean.csv` on `department_id` for Workforce & Staffing Efficiency (BQ 2) analysis.

---

### ðŸ‘¥ 3. Team Assignments & Role Model (Milestone 3)
The team operates using a two-role model (**Type A: Data Analysis / EDA + KPIs** and **Type B: Visualization & Dashboard Build**):

| # | Team Member | Type | Task | Business Question |
|---|-------------|------|------|-------------------|
| 1 | **Sirivalli Reddyvari** | Type A | Analyze Bed Utilization & Occupancy | Bed Utilization & Occupancy |
| 2 | **Tanvi Ajit Bhosale** | Type B | Visualize Bed Utilization & Occupancy | Bed Utilization & Occupancy |
| 3 | **Sowmitha A** | Type A | Analyze Workforce & Staffing Efficiency | Workforce & Staffing Efficiency |
| 4 | **Sarthak Jejurkar** | Type B | Visualize Workforce & Staffing Efficiency | Workforce & Staffing Efficiency |
| 5 | **Abhi** | Type A | Analyze Department-wise Resource Utilization | Department-wise Resource Utilization |
| 6 | **Rushikesh** | Type B | Visualize Department-wise Resource Utilization | Department-wise Resource Utilization |
| 7 | **Divya Kumari** | Type A | Analyze Benchmark & Capacity Gaps | Benchmark & Capacity Gap Analysis |
| 8 | **Deepika J** | Type B | Visualize Benchmark & Capacity Gaps | Benchmark & Capacity Gap Analysis |
| 9 | **Nafisa** | Type B | **Dashboard Integration Lead** | Assembles & integrates all pages (Pages 4 & 5) |
| 10 | **Keerthi Machanooru** | Lead | **Documentation & GitHub Lead** | GitHub README, PR merges, repository folder structure |

---

### ðŸ” 4. Business Question Pairings & Datasets

| Business Question | Type A (Analyst) | Type B (Visualizer) | Datasets Needed |
|-------------------|------------------|---------------------|-----------------|
| **1. Bed Utilization & Occupancy** | **Sirivalli Reddyvari** | **Tanvi Ajit Bhosale** | `admissions_clean.csv`, `departments_clean.csv`, `bed_capacity.csv` |
| **2. Workforce & Staffing Efficiency** | **Sowmitha A** | **Sarthak Jejurkar** | `admissions_clean.csv`, `doctors_preprocessed.csv`, `staff_capacity.csv` |
| **3. Department-wise Resource Utilization** | **Abhi** | **Rushikesh** | `admissions_clean.csv`, `departments_clean.csv`, `doctors_preprocessed.csv` |
| **4. Benchmark & Capacity Gap Analysis** | **Divya Kumari** | **Deepika J** | `admissions_clean.csv`, `bed_capacity.csv`, `doctors_preprocessed.csv` |
| **Dashboard Integration & Docs** | â€” | **Nafisa & Keerthi Machanooru** | All assembled datasets, notebooks, and dashboard scripts |

---

### ðŸ“‘ 5. Detailed Task Breakdown & KPIs

#### 1. Bed Utilization & Occupancy (Sirivalli Reddyvari âž” Tanvi Ajit Bhosale)
* Bed Occupancy Rate per department: `(Patient-days / Available bed-days) * 100`
* Available Beds per department: `Total_Beds - Occupied Beds`
* Identify overloaded departments vs. underutilized departments
* **Visualizations:** Department-wise occupancy rate chart, available-beds chart, KPI summary cards

#### 2. Workforce & Staffing Efficiency (Sowmitha A âž” Sarthak Jejurkar)
* Patients-per-Doctor Ratio: Overall and department-wise
* Patients-per-Staff Ratio: Overall and department-wise using `staff_capacity.csv`
* Department Workload: Admissions relative to available doctors + support staff
* **Visualizations:** Patients-per-doctor & patients-per-staff bar charts, interactive department filter

#### 3. Department-wise Resource Utilization (Abhi âž” Rushikesh)
* Combine bed capacity and doctor workforce data to classify departments
* Overall Resource Utilization Score combining bed occupancy and doctor workload
* Identify departments showing the clearest operational and resource strain
* **Visualizations:** Combined resource-utilization heatmap or ranked cross-department bar chart

#### 4. Benchmark & Capacity Gap Analysis (Divya Kumari âž” Deepika J)
* Compare actual operational utilization against `bed_capacity.csv` benchmarks
* Quantify the operational gap between actual and target utilization per department
* Flag departments exhibiting critical capacity shortfalls
* **Visualizations:** Benchmark vs. Actual comparison chart, capacity scorecard

#### 5. Dashboard Integration (Nafisa - Data Integration Lead)
* Assemble all Type B visualization outputs into unified multi-page Plotly Dash application
* Deliver **Page 4** (Bed Utilization & Workforce Efficiency) and **Page 5** (Resource Utilization & Capacity Benchmarks)

#### 6. GitHub Management & Documentation (Keerthi Machanooru - PR & GitHub Lead)
* Maintain GitHub folder hierarchy including `milestone3/` directory
* Review, resolve merge conflicts, and merge pull requests
* Update repository documentation and compile the presentation

---

### ðŸ“ 6. Repository `milestone3/` Structure
```
milestone3/
â”œâ”€â”€ README.md
â”œâ”€â”€ data/
â”‚   â”œâ”€â”€ processed/
â”‚   â””â”€â”€ raw/
â”œâ”€â”€ notebook/
â”‚   â”œâ”€â”€ Bed_Utilization_Occupancy_EDA.ipynb
â”‚   â”œâ”€â”€ Bed_Utilization_Occupancy_Visualization.ipynb
â”‚   â”œâ”€â”€ Department wise resource_utilization.ipynb
â”‚   â”œâ”€â”€ Department_wise_resource_utilization_visualization.ipynb
â”‚   â”œâ”€â”€ workforce_staffing_efficiency.ipynb
â”‚   â””â”€â”€ workforce_staffing_efficiency_visualization.ipynb
â”œâ”€â”€ report/
â”‚   â”œâ”€â”€ bed_utilization.html
â”‚   â”œâ”€â”€ bed_utilization_occupancy_dashboard.html
â”‚   â”œâ”€â”€ benchmark_capacity_gap.html
â”‚   â””â”€â”€ department_resource_utilization.html
â””â”€â”€ outputs/
    â””â”€â”€ .gitkeep
```

---

### ðŸš€ 7. How to Run the Complete Dashboard
```bash
git clone https://github.com/springboardmentor647/medical-operations-dashboard-team-a-batch1.git
cd medical-operations-dashboard-team-a-batch1
pip install dash plotly pandas numpy
python dashboard/app.py
```
Open [http://localhost:8050](http://localhost:8050/) in your web browser to interact with all 5 dashboard pages.

---

### ðŸ”ƒ 8. Milestone 3 PR & Merge Workflow (Managed by @Keerthi Machanooru)
* **Sirivalli Reddyvari** (`Sirivalli-Milestone-3` / PR #30) âž” Bed Utilization Analysis [Merged âœ…]
* **Rushikesh** (`feature/department-resource-utilization` / PR #31) âž” Department Resource Utilization [Merged âœ…]
* **Nafisa** (`nafisa-milestone3-dashboard-integration` / PR #32) âž” Multi-Page Dashboard Integration Lead (Pages 4 & 5) [Merged âœ…]
* **Tanvi Ajit Bhosale** (`Tanvii-08-milestone3` / PR #29 & PR #33) âž” Bed Utilization Visualizations [Merged âœ…]
* **Sarthak Jejurkar** (`Visualize-workforce-staffing-sarthak-jejurkar` / PR #27) âž” Workforce Staffing Visualizations [Merged âœ…]
* **Sowmitha A** (`sowmitha-analyze-workforce-staffing-m3`) âž” Workforce Staffing Analysis
* **Abhi** (`abhi-resource-utilization-analysis-m3`) âž” Resource Utilization Analysis
* **Divya Kumari** (`divya-benchmark-capacity-analysis-m3`) âž” Benchmark & Capacity Gap Analysis
* **Keerthi Machanooru** âž” Merge all PRs into `main`, maintain directory structure integrity, and update README.
