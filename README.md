# 🩺 Vaccination Data Analysis Project  

![Vaccination Dashboard Banner](https://img.icons8.com/?size=100&id=86785&format=png) 

# 🩺 Global Vaccination Data Analysis 🌍  
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Jupyter Notebook](https://img.shields.io/badge/Notebook-Jupyter-orange.svg)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow.svg)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen.svg)
 

A comprehensive data analytics project that explores **global vaccination coverage, disease incidence, and immunization performance** using **Python, SQLite, and Power BI**.  
This project demonstrates **ETL (Extract-Transform-Load)** workflows, SQL queries, and interactive **Power BI dashboards** to provide deep insights into vaccine trends.

---

## 📚 Table of Contents
1. [About the Project](#about-the-project)
2. [Dataset Details](#dataset-details)
3. [Project Structure](#project-structure)
4. [Key Insights](#key-insights)
5. [Tech Stack](#tech-stack)
6. [Dashboard Overview](#dashboard-overview)
7. [How to Run](#how-to-run)
8. [Author](#author)

---

## 🩸 About the Project
This project analyzes **global vaccination coverage trends**, identifies **drop-offs**, **booster uptake**, and **regional differences** in immunization performance.  
It integrates multiple datasets (country, vaccine introduction, coverage, and cases) into a unified database and visualizes them in Power BI.

---

## 📊 Dataset Details
| Table Name | Description |
|-------------|-------------|
| `dim_country` | Country & WHO region data |
| `dim_vaccine_intro` | Vaccine introduction timeline |
| `dim_schedule` | Age group & dose schedule details |
| `fact_coverage` | Coverage %, doses administered |
| `fact_cases` | Reported cases by disease |
| `fact_incidence` | Disease incidence rates |

---

## 🗂 Project Structure

Vaccination-Project/
│
├── data/
│ ├── data_raw/ # Raw Excel data files
│ ├── exports/ # Processed CSV tables
│
├── notebooks/
│ ├── vaccination_analysis.ipynb
│
├── reports/
│ ├── PowerBI_Dashboard.pbix
│
├── sql/
│ ├── schema.sql
│
├── README.md
├── LICENSE
└── Project_Description.md


---

## 🌍 Key Insights
- 💉 Average coverage improved by **15%** between 2010–2023.  
- 📉 Drop-off between **Dose1 & Dose2** identified in low-income regions.  
- 🔬 Booster uptake varied significantly across WHO regions.  
- 🌎 Power BI dashboard highlights **country-level coverage vs cases** correlation.

---

## 🛠 Tech Stack
- **Python (Pandas, SQLite, Matplotlib)**  
- **Power BI**  
- **Excel**  
- **SQL (Data Cleaning & Joins)**  

---

## 📈 Dashboard Overview
Power BI interactive visuals:
- Line Chart: Coverage Trends (by year)
- Map: WHO Region Coverage
- Bar Chart: Drop-off by Dose
- Table: Country-wise Vaccine Introduction

---

## 🚀 How to Run
1. Clone the repository  
2. Open the Jupyter Notebook `vaccination_analysis.ipynb`  
3. Run all cells to generate processed data  
4. Open `PowerBI_Dashboard.pbix` → Refresh data → View visuals  

---

## 👨‍💻 Author
**Created by:** Sayyed Mohsin Ali  
📧 Email: smohsin32@yahoo.in
🌐 GitHub: https://github.com/SayyedMohsin