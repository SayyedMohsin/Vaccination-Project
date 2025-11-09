import pandas as pd
import sqlite3
import os

# Database path
DB_PATH = "vaccination.db"

# Input files (inside data_raw)
FILES = {
    "coverage": "data_raw/coverage-data.xlsx",
    "incidence": "data_raw/incidence-rate-data.xlsx",
    "cases": "data_raw/reported-cases-data.xlsx",
    "intro": "data_raw/vaccine-introduction-data.xlsx",
    "schedule": "data_raw/vaccine-schedule-data.xlsx",
    "country": "data_raw/dim_country.csv"
}

def load_data():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found at {DB_PATH}. Run create_vax_db.py first.")

    conn = sqlite3.connect(DB_PATH)

    # 1. Load Coverage
    df_cov = pd.read_excel(FILES["coverage"])
    df_cov.to_sql("fact_coverage", conn, if_exists="replace", index=False)
    print("[OK] fact_coverage rows inserted:", len(df_cov))

    # 2. Load Incidence
    df_inc = pd.read_excel(FILES["incidence"])
    df_inc.to_sql("fact_incidence", conn, if_exists="replace", index=False)
    print("[OK] fact_incidence rows inserted:", len(df_inc))

    # 3. Load Reported Cases
    df_cases = pd.read_excel(FILES["cases"])
    df_cases.to_sql("fact_cases", conn, if_exists="replace", index=False)
    print("[OK] fact_cases rows inserted:", len(df_cases))

    # 4. Load Vaccine Introduction
    df_intro = pd.read_excel(FILES["intro"])
    df_intro.to_sql("dim_vaccine_intro", conn, if_exists="replace", index=False)
    print("[OK] dim_vaccine_intro rows inserted:", len(df_intro))

    # 5. Load Schedule
    df_sch = pd.read_excel(FILES["schedule"])
    df_sch.to_sql("dim_schedule", conn, if_exists="replace", index=False)
    print("[OK] dim_schedule rows inserted:", len(df_sch))

    # 6. Load Country Master
    df_country = pd.read_csv(FILES["country"])
    df_country.to_sql("dim_country", conn, if_exists="replace", index=False)
    print("[OK] dim_country rows inserted:", len(df_country))

    conn.commit()
    conn.close()
    print("[SUCCESS] All files loaded into DB:", DB_PATH)


if __name__ == "__main__":
    load_data()
