import os
import sqlite3
import pandas as pd

# -------------------------
# Paths Setup
# -------------------------
RAW_DIR = "data_raw"
EXPORT_DIR = "exports"
DB_PATH = "vaccination.db"

os.makedirs(EXPORT_DIR, exist_ok=True)

# -------------------------
# File Mapping
# -------------------------
FILES = {
    "coverage": os.path.join(RAW_DIR, "coverage-data.xlsx"),
    "incidence": os.path.join(RAW_DIR, "incidence-rate-data.xlsx"),
    "cases": os.path.join(RAW_DIR, "reported-cases-data.xlsx"),
    "intro": os.path.join(RAW_DIR, "vaccine-introduction-data.xlsx"),
    "schedule": os.path.join(RAW_DIR, "vaccine-schedule-data.xlsx"),
}

# -------------------------
# Load + Rename Columns
# -------------------------

def load_coverage():
    df = pd.read_excel(FILES["coverage"])
    df = df.rename(columns={
        "GROUP": "group_col",
        "CODE": "iso3",
        "NAME": "country_name",
        "YEAR": "year",
        "ANTIGEN": "antigen",
        "ANTIGEN_DESCRIPTION": "antigen_desc",
        "COVERAGE_CATEGORY": "coverage_category",
        "COVERAGE_CATEGORY_DESCRIPTION": "coverage_category_desc",
        "TARGET_NUMBER": "target_number",
        "DOSES": "doses_administered",
        "COVERAGE": "coverage_percent"
    })
    return df

def load_incidence():
    df = pd.read_excel(FILES["incidence"])
    df = df.rename(columns={
        "GROUP": "group_col",
        "CODE": "iso3",
        "NAME": "country_name",
        "YEAR": "year",
        "DISEASE": "disease",
        "DISEASE_DESCRIPTION": "disease_desc",
        "DENOMINATOR": "denominator",
        "INCIDENCE_RATE": "incidence_rate"
    })
    return df

def load_cases():
    df = pd.read_excel(FILES["cases"])
    df = df.rename(columns={
        "GROUP": "group_col",
        "CODE": "iso3",
        "NAME": "country_name",
        "YEAR": "year",
        "DISEASE": "disease",
        "DISEASE_DESCRIPTION": "disease_desc",
        "CASES": "cases"
    })
    return df

def load_intro():
    df = pd.read_excel(FILES["intro"])
    df = df.rename(columns={
        "ISO_3_CODE": "iso3",
        "COUNTRYNAME": "country_name",
        "WHO_REGION": "who_region",
        "YEAR": "intro_year",
        "DESCRIPTION": "antigen",
        "INTRO": "intro_flag"
    })
    return df

def load_schedule():
    df = pd.read_excel(FILES["schedule"])
    df = df.rename(columns={
        "ISO_3_CODE": "iso3",
        "COUNTRYNAME": "country_name",
        "WHO_REGION": "who_region",
        "YEAR": "year",
        "VACCINECODE": "antigen_code",
        "VACCINE_DESCRIPTION": "antigen_desc",
        "SCHEDULEROUNDS": "schedule_round",
        "TARGETPOP": "target_pop",
        "TARGETPOP_DESCRIPTION": "target_pop_desc",
        "GEOAREA": "geoarea",
        "AGEADMINISTERED": "age_admin",
        "SOURCECOMMENT": "source_comment"
    })
    return df

# -------------------------
# Save to SQLite + CSV
# -------------------------
def save_to_db_and_csv(df, name, conn):
    df.to_sql(name, conn, if_exists="replace", index=False)
    export_path = os.path.join(EXPORT_DIR, f"{name}.csv")
    df.to_csv(export_path, index=False)
    print(f"[OK] {name}: rows={len(df)} → saved {export_path}")

# -------------------------
# Main
# -------------------------
def main():
    conn = sqlite3.connect(DB_PATH)

    save_to_db_and_csv(load_coverage(), "fact_coverage", conn)
    save_to_db_and_csv(load_incidence(), "fact_incidence", conn)
    save_to_db_and_csv(load_cases(), "fact_cases", conn)
    save_to_db_and_csv(load_intro(), "dim_vaccine_intro", conn)
    save_to_db_and_csv(load_schedule(), "dim_schedule", conn)

    conn.close()
    print("\n[SUCCESS] Database + CSV export completed.")

if __name__ == "__main__":
    main()
