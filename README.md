# Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics Group 1

## Project Overview
The **Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics Group 1** is a healthcare analytics project developed as part of the **Infosys Springboard Internship**. The project focuses on collecting, preprocessing, integrating, and analyzing healthcare datasets to generate meaningful insights and support dashboard development.

### Objectives

* Collect healthcare datasets.
* * Clean and preprocess the datasets.
  * * Integrate multiple datasets into a unified dataset.
    * * Generate Key Performance Indicators (KPIs).
      * * Perform trend analysis.
        * * Build a dashboard for healthcare insights.
          * * Maintain the project using GitHub.
           
            * ### Technologies Used
           
            * * Python
              * * Pandas
                * * NumPy
                  * * Jupyter Notebook
                    * * Git
                      * * GitHub
                       
                        * ---
                       
                        * ## Project Structure
                        * ```
                          medical-operations-dashboard-team-a-batch1
                          |
                          -- data/
                          |   -- raw/
                          -- notebooks/
                          -- src/
                          -- README.md
                          ```

                          ---

                          ## Datasets Used

                          * admissions.csv
                          * * billing.csv
                            * * departments.csv
                              * * doctors.csv
                                * * lab_results.csv
                                  * * medications.csv
                                    * * patients.csv
                                      * * raw_surgeries.csv
                                       
                                        * ---
                                       
                                        * ## Project Workflow
                                       
                                        * 1. Data Collection
                                          2. 2. Data Preprocessing
                                             3. 3. Data Integration
                                                4. 4. KPI Generation
                                                   5. 5. Trend Analysis
                                                      6. 6. Documentation & GitHub
                                                         7. 7. Dashboard Development
                                                           
                                                            8. ---
                                                           
                                                            9. ## Team Members
                                                            10. | Team Member | Responsibility |
                                                            11. |-------------|----------------|
                                                            12. | Sowmitha | Data Collection, Documentation & GitHub |
                                                            13. | Tanvi Bhosale | Data Preprocessing (Patients Dataset) |
                                                            14. | Sarthak | Data Preprocessing (Lab & Billing Datasets) |
                                                            15. | Sirivalli Reddyvari | Data Preprocessing (Doctors Dataset) |
                                                            16. | Nafisa | Data Preprocessing (Departments & Admissions Datasets) |
                                                            17. | Divya Kumari | Data Integration |
                                                            18. | Rushikesh | Data Preprocessing (Surgery Dataset) |
                                                            19. | Indhumathi K | Data Preprocessing (Medications Dataset) |
                                                            20. | Deepika J | KPI Generation |
                                                            21. | Abhi | Trend Analysis |
                                                           
                                                            22. ---
                                                           
                                                            23. ## Team
                                                            24. ### Milestone 1 Completed
                                                           
                                                            25. * Data Collection
                                                                * * Data Preprocessing
                                                                  * * Data Integration
                                                                    * * KPI Generation
                                                                      * * Trend Analysis
                                                                        * * GitHub Collaboration
                                                                          * * Documentation
                                                                           
                                                                            * ### Future Work
                                                                            * * Develop an interactive Power BI Dashboard.
                                                                              * * Create advanced healthcare visualizations.
                                                                                * * Enhance KPI reporting.
                                                                                  * * Improve operational insights.
                                                                                   
                                                                                    * ### License
                                                                                    * This project was developed for educational purposes as part of the Infosys Springboard Internship.
                                                                                   
                                                                                    * ---
                                                                                   
                                                                                * ## ** ---- Milestone 2 - Patient Flow & Service Demand Intelligence -----**
                                                                               
                                                                                * ### 1. Project Overview
                                                                                * Milestone 2 focuses on transforming the cleaned healthcare datasets prepared during Milestone 1 into meaningful operational insights.
                                                                                * The team performs Exploratory Data Analysis (EDA), KPI generation, trend analysis, visualization, and dashboard development to support healthcare operational decision-making.
                                                                               
                                                                                * ### 2. Milestone 2 Objective
                                                                                * The main objective of Milestone 2 is to analyze patient flow and healthcare service demand and convert the results into interactive dashboard insights.
                                                                                * #### Objectives
                                                                               
                                                                                * * Analyze admission and discharge patterns.
                                                                                  * * Analyze department-wise patient workload.
                                                                                    * * Monitor treatment and service demand.
                                                                                      * * Identify operational bottlenecks and capacity strain.
                                                                                        * * Analyze surgery workload.
                                                                                          * * Generate KPIs and trends.
                                                                                            * * Develop visualizations for dashboard integration.
                                                                                             
                                                                                              * ### 3. Business Questions
                                                                                              * Milestone 2 is organized around six core business questions:
                                                                                             
                                                                                              * 1. Admission Trends
                                                                                                2. 2. Department-wise Patient Load
                                                                                                   3. 3. Patient Discharge & Flow
                                                                                                      4. 4. Treatment & Service Demand
                                                                                                         5. 5. Bottlenecks & Capacity Strain
                                                                                                            6. 6. Surgery Workload
                                                                                                              
                                                                                                               7. ---
                                                                                                              
                                                                                                         6. ## ** ---- Milestone 3 - Resource Utilization & Capacity Intelligence Module -----**
                                                                                                        
                                                                                                         7. ### 1. Milestone 3 Overview & Objective
                                                                                                         8. **Weeks 5-6 | Team of 10**
                                                                                                        
                                                                                                         9. Milestone 3 focuses on **Resource Utilization & Capacity Intelligence** - developing healthcare resource intelligence dashboards and capacity monitoring capabilities covering bed utilization, workforce efficiency, department-wise resource distribution, and benchmark/capacity gap analysis.
                                                                                                        
                                                                                                         10. ---
                                                                                                        
                                                                                                         11. ### 2. Data Notes - Benchmark Gap Datasets (Resolved)
                                                                                                        
                                                                                                         12. 1. **Bed Capacity Gap (data/raw/bed_capacity.csv)**:
                                                                                                             2.    - Contents: department_id, department_name, Total_Beds (one row per department)
                                                                                                                   -    - Purpose: Benchmark bed counts defined by the team to allow Bed Utilization (BQ 1) calculation.
                                                                                                                        -    - Usage: Joined against admissions_clean.csv on department_id to compute occupancy and available beds.
                                                                                                                         
                                                                                                                             - 2. **Staff Capacity Gap (data/raw/staff_capacity.csv)**:
                                                                                                                               3.    - Contents: department_id, department_name, Total_Staff (one row per department)
                                                                                                                                     -    - Purpose: Benchmark staff counts representing full healthcare staffing.
                                                                                                                                          -    - Usage: Joined against doctors_preprocessed.csv and admissions_clean.csv on department_id for Workforce & Staffing Efficiency (BQ 2) analysis.
                                                                                                                                           
                                                                                                                                               - ---
                                                                                                                                               
                                                                                                                                               ### 3. Team Assignments & Role Model (Milestone 3)
                                                                                                                                               
                                                                                                                                               The team operates using a two-role model (Type A: Data Analysis / EDA + KPIs and Type B: Visualization & Dashboard Build):
                                                                                                                                               
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
                                                                                                                                               
                                                                                                                                               ### 4. Business Question Pairings & Datasets
                                                                                                                                               
                                                                                                                                               | Business Question | Type A (Analyst) | Type B (Visualizer) | Datasets Needed |
                                                                                                                                               |-------------------|------------------|---------------------|------------------|
                                                                                                                                               | **1. Bed Utilization & Occupancy** | **Sirivalli Reddyvari** | **Tanvi Ajit Bhosale** | admissions_clean.csv, departments_clean.csv, bed_capacity.csv |
                                                                                                                                               | **2. Workforce & Staffing Efficiency** | **Sowmitha A** | **Sarthak Jejurkar** | admissions_clean.csv, doctors_preprocessed.csv, staff_capacity.csv |
                                                                                                                                               | **3. Department-wise Resource Utilization** | **Abhi** | **Rushikesh** | admissions_clean.csv, departments_clean.csv, doctors_preprocessed.csv |
                                                                                                                                               | **4. Benchmark & Capacity Gap Analysis** | **Divya Kumari** | **Deepika J** | admissions_clean.csv, bed_capacity.csv, doctors_preprocessed.csv |
                                                                                                                                               | **Dashboard Integration & Docs** | - | **Nafisa & Keerthi Machanooru** | All assembled datasets, notebooks, and dashboard scripts |
                                                                                                                                               
                                                                                                                                               ---
                                                                                                                                               
                                                                                                                                               ### 5. Detailed Task Breakdown & KPIs
                                                                                                                                               
                                                                                                                                               #### 1. Bed Utilization & Occupancy (Sirivalli Reddyvari -> Tanvi Ajit Bhosale)
                                                                                                                                               - Bed Occupancy Rate per department: (Patient-days / Available bed-days) * 100
                                                                                                                                               - - Available Beds per department: Total_Beds - Occupied Beds
                                                                                                                                                 - - Identify overloaded departments vs. underutilized departments
                                                                                                                                                   - - Visualizations: Department-wise occupancy rate chart, available-beds chart, KPI summary cards
                                                                                                                                                    
                                                                                                                                                     - #### 2. Workforce & Staffing Efficiency (Sowmitha A -> Sarthak Jejurkar)
                                                                                                                                                     - - Patients-per-Doctor Ratio: Overall and department-wise
                                                                                                                                                       - - Patients-per-Staff Ratio: Overall and department-wise using staff_capacity.csv
                                                                                                                                                         - - Department Workload: Admissions relative to available doctors + support staff
                                                                                                                                                           - - Visualizations: Patients-per-doctor & patients-per-staff bar charts, interactive department filter
                                                                                                                                                            
                                                                                                                                                           - #### 3. Department-wise Resource Utilization (Abhi -> Rushikesh)
                                                                                                                                                           - - Combine bed capacity and doctor workforce data to classify departments
                                                                                                                                                             - - Overall Resource Utilization Score combining bed occupancy and doctor workload
                                                                                                                                                               - - Identify departments showing the clearest operational and resource strain
                                                                                                                                                                 - - Visualizations: Combined resource-utilization heatmap or ranked cross-department bar chart
                                                                                                                                                                  
                                                                                                                                                                   - #### 4. Benchmark & Capacity Gap Analysis (Divya Kumari -> Deepika J)
                                                                                                                                                                   - - Compare actual operational utilization against bed_capacity.csv benchmarks
                                                                                                                                                                     - - Quantify the operational gap between actual and target utilization per department
                                                                                                                                                                       - - Flag departments exhibiting critical capacity shortfalls
                                                                                                                                                                         - - Visualizations: Benchmark vs. Actual comparison chart, capacity scorecard
                                                                                                                                                                          
                                                                                                                                                                           - #### 5. Dashboard Integration (Nafisa - Data Integration Lead)
                                                                                                                                                                           - - Assemble all Type B visualization outputs into unified multi-page Plotly Dash application
                                                                                                                                                                             - - Deliver Page 4 (Bed Utilization & Workforce Efficiency) and Page 5 (Resource Utilization & Capacity Benchmarks)
                                                                                                                                                                              
                                                                                                                                                                               - #### 6. GitHub Management & Documentation (Keerthi Machanooru - PR & GitHub Lead)
                                                                                                                                                                               - - Maintain GitHub folder hierarchy including milestone3/ directory
                                                                                                                                                                                 - - Review, resolve merge conflicts, and merge pull requests
                                                                                                                                                                                   - - Update repository documentation and compile the presentation
                                                                                                                                                                                    
                                                                                                                                                                                     - ---
                                                                                                                                                                                     
                                                                                                                                                                                     ### 6. Repository milestone3/ Structure
                                                                                                                                                                                     
                                                                                                                                                                                     ```
                                                                                                                                                                                     milestone3/
                                                                                                                                                                                     -- README.md
                                                                                                                                                                                     -- analysis/
                                                                                                                                                                                     |   -- sowmitha_workforce_staffing_analysis.ipynb
                                                                                                                                                                                     |   -- sirivalli_bed_utilization_analysis.ipynb
                                                                                                                                                                                     |   -- abhi_resource_utilization_analysis.ipynb
                                                                                                                                                                                     |   -- divya_benchmark_capacity_analysis.ipynb
                                                                                                                                                                                     -- visualizations/
                                                                                                                                                                                     |   -- tanvi_bed_utilization_visualization.ipynb
                                                                                                                                                                                     |   -- sarthak_workforce_staffing_visualization.ipynb
                                                                                                                                                                                     |   -- rushikesh_resource_utilization_visualization.ipynb
                                                                                                                                                                                     |   -- deepika_benchmark_capacity_visualization.ipynb
                                                                                                                                                                                     -- data_integration/
                                                                                                                                                                                     |   -- nafisa_milestone3_data_integration.ipynb
                                                                                                                                                                                     -- outputs/
                                                                                                                                                                                         -- .gitkeep
                                                                                                                                                                                     ```
                                                                                                                                                                                     
                                                                                                                                                                                     ---
                                                                                                                                                                                     
                                                                                                                                                                                     ### 7. How to Run the Complete Dashboard
                                                                                                                                                                                     
                                                                                                                                                                                     ```bash
                                                                                                                                                                                     git clone https://github.com/springboardmentor647/medical-operations-dashboard-team-a-batch1.git
                                                                                                                                                                                     cd medical-operations-dashboard-team-a-batch1
                                                                                                                                                                                     pip install dash plotly pandas numpy
                                                                                                                                                                                     python dashboard/app.py
                                                                                                                                                                                     ```
                                                                                                                                                                                     Open http://localhost:8050 in your web browser to interact with all 5 dashboard pages.
                                                                                                                                                                                     
                                                                                                                                                                                     ---
                                                                                                                                                                                     
                                                                                                                                                                                     ### 8. Milestone 3 PR & Merge Workflow (Managed by @Keerthi Machanooru)
                                                                                                                                                                                     
                                                                                                                                                                                     1. **Sirivalli Reddyvari** (Sirivalli-Milestone-3 / PR #30) -> Bed Utilization Analysis
                                                                                                                                                                                     2. 2. **Rushikesh** (feature/department-resource-utilization / PR #31) -> Department Resource Utilization
                                                                                                                                                                                        3. 3. **Sowmitha A** (sowmitha-analyze-workforce-staffing-m3) -> Workforce Staffing Analysis
                                                                                                                                                                                           4. 4. **Tanvi Ajit Bhosale** (tanvi-visualize-bed-utilization-m3) -> Bed Utilization Visualizations
                                                                                                                                                                                              5. 5. **Sarthak Jejurkar** (sarthak-visualize-workforce-staffing-m3) -> Workforce Staffing Visualizations
                                                                                                                                                                                                 6. 6. **Abhi** (abhi-resource-utilization-analysis-m3) -> Resource Utilization Analysis
                                                                                                                                                                                                    7. 7. **Divya Kumari** (divya-benchmark-capacity-analysis-m3) -> Benchmark & Capacity Gap Analysis
                                                                                                                                                                                                       8. 8. **Nafisa** (nafisa-milestone3-dashboard-integration / PR #32) -> Multi-Page Dashboard Integration Lead (Pages 4 & 5)
                                                                                                                                                                                                          9. 9. **Keerthi Machanooru** -> Merge all PRs into main, verify directory structure integrity, and update README.
                                                                                                                                                                                                             10. 
