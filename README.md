🏥 Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics Group 1
📌 Project Overview
The **Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics Group 1** is a healthcare analytics project developed as part of the **Infosys Springboard Internship**. The project focuses on collecting, preprocessing, integrating, and analyzing healthcare datasets to generate meaningful insights and support dashboard development.

Objectives

* Collect healthcare datasets.
* Clean and preprocess the datasets.
* Integrate multiple datasets into a unified dataset.
* Generate Key Performance Indicators (KPIs).
* Perform trend analysis.
* Build a dashboard for healthcare insights.
* Maintain the project using GitHub.

Technologies Used

* Python
* Pandas
* NumPy
* Jupyter Notebook
* Git
* GitHub

📂 Project Structure
medical-operations-dashboard-team-a-batch2
│
├── data/
│   └── raw/
├── notebooks/
├── src/
├── README.md

📊 Datasets Used

* admissions.csv
* billing.csv
* departments.csv
* doctors.csv
* lab\_results.csv
* medications.csv
* patients.csv
* raw\_surgeries.csv

🔄 Project Workflow

1. Data Collection
2. Data Preprocessing
3. Data Integration
4. KPI Generation
5. Trend Analysis
6. Documentation \& GitHub
7. Dashboard Development
👥 Team Members
| Team Member | Responsibility |
|-------------|----------------|
| Sowmitha | Data Collection, Documentation \& GitHub |
| Tanvi Bhosale | Data Preprocessing (Patients Dataset) |
| Sarthak | Data Preprocessing (Lab \& Billing Datasets) |
| Sirivalli Reddyvari | Data Preprocessing (Doctors Dataset) |
| Nafisa | Data Preprocessing (Departments \& Admissions Datasets) |
| Divya Kumari | Data Integration |
| Rushikesh | Data Preprocessing (Surgery Dataset) |
| Indhumathi K | Data Preprocessing (Medications Dataset) |
| Deepika J | KPI Generation |
| Abhi | Trend Analysis |

👥 Team
Milestone 1 Completed

* Data Collection
* Data Preprocessing
* Data Integration
* KPI Generation
* Trend Analysis
* GitHub Collaboration
* Documentation
🚀 Future Work
* Develop an interactive Power BI Dashboard.
* Create advanced healthcare visualizations.
* Enhance KPI reporting.
* Improve operational insights.
📜 License
This project was developed for educational purposes as part of the Infosys Springboard Internship.

\*\* ---- Milestone 2 – Patient Flow \& Service Demand Intelligence -----\*\*

📌1. Project Overview
Milestone 2 focuses on transforming the cleaned healthcare datasets prepared during Milestone 1 into meaningful operational insights.
The team performs Exploratory Data Analysis (EDA), KPI generation, trend analysis, visualization, and dashboard development to support healthcare operational decision-making.

🔍 2. Milestone 2 Objective
The main objective of Milestone 2 is to analyze patient flow and healthcare service demand and convert the results into interactive dashboard insights.
Objectives

* Analyze admission and discharge patterns.
* Analyze department-wise patient workload.
* Monitor treatment and service demand.
* Identify operational bottlenecks and capacity strain.
* Analyze surgery workload.
* Generate KPIs and trends.
* Develop visualizations for dashboard integration.

🤖3. Business Questions
Milestone 2 is organized around six core business questions:

1. Admission Trends
2. Department-wise Patient Load
3. Patient Discharge \& Flow
4. Treatment \& Service Demand
5. Bottlenecks \& Capacity Strain
6. Surgery Workload
Each business question is handled by one Type A and one Type B team member.

🗒️4. Task Division

|Business Question|Type A – Analysis|Type B – Visualization|
|-|-|-|
|Admission Trends|Divya|Nafisa|
|Department-wise Patient Load|Srivalli|Tanvi|
|Patient Discharge \& Flow|Sowmitha|Keerthi|
|Treatment \& Service Demand|Abhinay|Sarthak|
|Bottlenecks \& Capacity Strain|Sarthak|Sarthak|
|Surgery Workload|Deepika|Aarthi|
|Dashboard Integration|Nafisa||
|Documentation|Sowmitha||
|Type A members perform EDA and KPI analysis, while Type B members convert the findings into visualizations and dashboard components.|||
| Business Question | Type A – Analysis | Type B – Visualization |
|---|---|---|
| Admission Trends | Divya | Nafisa |
| Department-wise Patient Load | Srivalli | Tanvi |
| Patient Discharge & Flow | Sowmitha | Keerthi  |
| Treatment & Service Demand | Abhinay | Sarthak |
| Bottlenecks & Capacity Strain | Sarthak | Sarthak |
| Surgery Workload | Deepika | Divya |
| Dashboard Integration |  Nafisa  |
| Documentation | Sowmitha |
Type A members perform EDA and KPI analysis, while Type B members convert the findings into visualizations and dashboard components.

📂5. Datasets Used
Admission Trends

* admissions\_clean.csv

Department-wise Patient Load

* admissions\_clean.csv
* departments\_clean.csv

Patient Discharge \& Flow

* admissions\_clean.csv

Treatment \& Service Demand

* lab\_results\_clean.csv
* billing\_clean.csv

Bottlenecks \& Capacity Strain

* admissions\_clean.csv
* doctors\_preprocessed.csv
* departments\_clean.csv

Surgery Workload

* surgeries\_clean\_fixed.csv

📜 6. Analysis Methodology
The Milestone 2 workflow follows:
Data Loading
→ Data Validation
→ Exploratory Data Analysis
→ KPI Generation
→ Trend Analysis
→ Findings
→ Visualization
→ Dashboard Integration
Python and Pandas are used for data analysis and KPI generation.

⬇️ 7. Patient Discharge \& Flow Analysis
For the Patient Discharge \& Flow business question, the analysis uses:

* Discharge\_Date
* Status
* Length\_of\_Stay\_Days
The analysis focuses on the admission-to-discharge timeline and patient status transitions.
Since no movement or transfer log is available, ward-to-ward patient movement is not analyzed.

📊 KPIs Generated

* Total Patients
* Average Length of Stay
* Discharge Rate
* Patient Status Distribution
* Monthly Admissions
* Monthly Discharges
* Department-wise Admissions
* Department-wise Discharges
* Department-wise Discharge Rate

🔑Key Results

* Total Patients: 5,000
* Average Length of Stay: 5.52 days
* Discharge Rate: 24.28%
* Critical Patients: 1,279
* Under Treatment: 1,272
* Recovered Patients: 1,235
* Discharged Patients: 1,214
* Highest Monthly Admissions: July – 524
* Highest Monthly Discharges: March – 584
* Highest Department Admissions: D015 – 335
* Highest Department Discharge Rate: D004 – 30.32%

📈 8. Visualization
The Type B members use the KPI outputs and findings from Type A analysis to create dashboard visualizations.
Planned visualizations include:

* Admission trend charts
* Department-wise workload charts
* Patient status distribution
* Monthly admission and discharge trends
* Length of Stay analysis
* Treatment and service demand charts
* Bottleneck and capacity indicators
* Surgery workload visualizations

⚙️9. Tools \& Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Plotly / Dash or Power BI
* Google Colab
* Git
* GitHub

🔄️10. GitHub Workflow
The team uses GitHub for collaborative development and documentation.
Workflow:
Clone Repository
→ Create/Use Working Branch
→ Perform Analysis
→ Commit Changes
→ Push Changes
→ Review/Integrate
→ Dashboard Assembly
Work is pushed regularly so that dashboard integration can happen smoothly.

⚠️11. Challenges \& Solutions
Challenge 1: Different Business Questions
The team had multiple analytical requirements.
**Solution:** Tasks were divided into six business questions with dedicated Type A and Type B members.
Challenge 2: Missing Patient Movement Data
No ward-to-ward movement or transfer log was available.
**Solution:** Patient flow was analyzed using admission-to-discharge timelines and status transitions.
Challenge 3: Multiple Dataset Requirements
Some business questions required more than one dataset.
**Solution:** Relevant datasets were mapped to each business question and joined where required.
Challenge 4: Dashboard Integration
Different members produced separate analytical outputs.
**Solution:** Type A members provide KPI numbers and findings to Type B members for visualization and dashboard integration.

📦12. Milestone 2 Deliverables

* EDA and KPI analysis notebooks
* Business-question-specific findings
* KPI summary tables
* Visualization outputs
* Dashboard components
* GitHub updates
* README documentation



**Final integrated dashboard**
## 🚀 How to Run the Dashboard
---

* 
* 1\. Clone the repo and navigate to the project root
* 2\. Create and activate a virtual environment:
* &#x20;  python -m venv venv
* &#x20;  venv\\Scripts\\activate      # Windows
* &#x20;  source venv/bin/activate   # Mac/Linux
* 3\. Install dependencies:
* &#x20;  pip install dash plotly pandas
* 4\. Run the app:
* &#x20;  python dashboard/app.py
* 5\. Open http://localhost:8050 in your browser
* 6\. Use the nav links at the top (Page 1, 2, 3) to view each business question's visualizations
* 
* \### Status
* \- Page 1: Admission Trends + Department-wise Patient Load ✅
* \- Page 2: Patient Discharge \& Flow + Treatment \& Service Demand ✅
* \- Page 3: Bottlenecks \& Capacity Strain ✅, Surgery Workload ✅

🔮13. Future Work

* Complete dashboard integration.
* Improve interactive visualizations.
* Add advanced operational indicators.
* Validate all KPI outputs.
* Finalize documentation and presentation.
* Integrate all business-question outputs into the final dashboard.

🎯14. Conclusion
Milestone 2 transforms the cleaned healthcare datasets from Milestone 1 into actionable operational intelligence.
Through EDA, KPI generation, trend analysis, visualization, and dashboard integration, the project provides insights into patient flow, service demand, workload, operational bottlenecks, and surgery workload.
The completed outputs will serve as the foundation for the final Medical Operations Intelligence Dashboard.

