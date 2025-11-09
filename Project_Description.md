# Vaccination Data Analysis – Project Summary

This project explores global vaccination performance using data analytics and visualization.  
It aims to identify coverage patterns, drop-offs between doses, and booster uptake trends across regions.  
The data pipeline integrates raw Excel datasets into a clean, structured SQLite database, enabling multi-dimensional analysis through SQL and Python.

The project performs 30+ analytical queries covering:
- Vaccine coverage by country and year
- Drop-off and booster uptake analysis
- Correlation between vaccination coverage and disease incidence
- Regional and temporal performance trends

The cleaned datasets are visualized through Power BI dashboards that offer interactive charts, line graphs, and maps for decision-making support.  
Each page of the dashboard focuses on a specific KPI—coverage, regional comparison, and introduction timelines.  

Technically, the workflow demonstrates an end-to-end ETL pipeline:
1. **Extract** raw Excel files into pandas DataFrames  
2. **Transform** using data cleaning, aggregation, and relational joins  
3. **Load** processed results into SQLite and Power BI  

The outcome is a dynamic, data-driven insight into global immunization efforts—helping researchers, policy makers, and analysts understand vaccination progress in a clear, visual, and actionable way.
