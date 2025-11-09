import os
import sqlite3
import pandas as pd

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "data_raw")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")
DB_PATH = os.path.join(BASE_DIR, "vaccination.db")

os.makedirs(EXPORT_DIR, exist_ok=True)

# Input files
FILES = {
    "coverage": os.path.join(RAW_DIR, "coverage-data.xlsx"),
    "incidence": os.path.join(RAW_DIR, "incidence-rate-data.xlsx"),
    "cases": os.path.join(RAW_DIR, "reported-cases-data.xlsx"),
    "intro": os.path.join(RAW_DIR, "vaccine-introduction-data.xlsx"),
    "schedule": os.path.join(RAW_DIR, "vaccine-schedule-data.xlsx"),
    "country": os.path.join(RAW_DIR, "dim_country.csv")  # already CSV
}

# Load function
def load_and_export():
    conn = sqlite3.connect(DB_PATH)

    # Coverage
    df_cov = pd.read_excel(FILES["coverage"])
    df_cov.to_sql("fact_coverage", conn, if_exists="replace", index=False)
    df_cov.to_csv(os.path.join(EXPORT_DIR, "fact_coverage.csv"), index=False)
    print("[OK] fact_coverage → DB + CSV")

    # Incidence
    df_inc = pd.read_excel(FILES["incidence"])
    df_inc.to_sql("fact_incidence", conn, if_exists="replace", index=False)
    df_inc.to_csv(os.path.join(EXPORT_DIR, "fact_incidence.csv"), index=False)
    print("[OK] fact_incidence → DB + CSV")

    # Reported cases
    df_cases = pd.read_excel(FILES["cases"])
    df_cases.to_sql("fact_cases", conn, if_exists="replace", index=False)
    df_cases.to_csv(os.path.join(EXPORT_DIR, "fact_cases.csv"), index=False)
    print("[OK] fact_cases → DB + CSV")

    # Vaccine intro
    df_intro = pd.read_excel(FILES["intro"])
    df_intro.to_sql("dim_vaccine_intro", conn, if_exists="replace", index=False)
    df_intro.to_csv(os.path.join(EXPORT_DIR, "dim_vaccine_intro.csv"), index=False)
    print("[OK] dim_vaccine_intro → DB + CSV")

    # Schedule
    df_sch = pd.read_excel(FILES["schedule"])
    df_sch.to_sql("dim_schedule", conn, if_exists="replace", index=False)
    df_sch.to_csv(os.path.join(EXPORT_DIR, "dim_schedule.csv"), index=False)
    print("[OK] dim_schedule → DB + CSV")

    # Country
    df_country = pd.read_csv(FILES["country"])
    df_country.to_sql("dim_country", conn, if_exists="replace", index=False)
    df_country.to_csv(os.path.join(EXPORT_DIR, "dim_country.csv"), index=False)
    print("[OK] dim_country → DB + CSV")

    conn.close()
    print("\n[SUCCESS] All data loaded into DB and exported as CSVs in 'exports/'")

# Run
if __name__ == "__main__":
    load_and_export()
