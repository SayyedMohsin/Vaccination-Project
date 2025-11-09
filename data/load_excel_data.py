import pandas as pd
import sqlite3
import os

DB_PATH = "vaccination.db"
DATA_DIR = "data_raw"

FILES = {
    "coverage": os.path.join(DATA_DIR, "coverage-data.xlsx"),
    "incidence": os.path.join(DATA_DIR, "incidence-rate-data.xlsx"),
    "cases": os.path.join(DATA_DIR, "reported-cases-data.xlsx"),
    "intro": os.path.join(DATA_DIR, "vaccine-introduction-data.xlsx"),
    "schedule": os.path.join(DATA_DIR, "vaccine-schedule-data.xlsx"),
}

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)

# Load Coverage
df_cov = pd.read_excel(FILES["coverage"])
df_cov.to_sql("fact_coverage", conn, if_exists="replace", index=False)

# Load Incidence
df_inc = pd.read_excel(FILES["incidence"])
df_inc.to_sql("fact_incidence", conn, if_exists="replace", index=False)

# Load Cases
df_cases = pd.read_excel(FILES["cases"])
df_cases.to_sql("fact_cases", conn, if_exists="replace", index=False)

# Load Vaccine Intro
df_intro = pd.read_excel(FILES["intro"])
df_intro.to_sql("dim_vaccine_intro", conn, if_exists="replace", index=False)

# Load Schedule
df_sched = pd.read_excel(FILES["schedule"])
df_sched.to_sql("dim_schedule", conn, if_exists="replace", index=False)

conn.close()
print("[SUCCESS] All Excel files loaded into vaccination.db")
