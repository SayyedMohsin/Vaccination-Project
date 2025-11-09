# create_vax_db.py
# Usage: python create_vax_db.py
import os
import sqlite3

HERE = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(HERE, "vaccination.db")

SCHEMA = """
-- Countries & Regions (normalized)
CREATE TABLE IF NOT EXISTS dim_country (
  iso3 TEXT PRIMARY KEY,
  country_name TEXT,
  who_region TEXT
);

-- Coverage (per country-year-antigen-dose/category)
CREATE TABLE IF NOT EXISTS fact_coverage (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  group_col TEXT,
  iso3 TEXT,
  country_name TEXT,
  year INTEGER,
  antigen TEXT,
  antigen_desc TEXT,
  coverage_category TEXT,
  coverage_category_desc TEXT,
  target_number REAL,
  doses_administered REAL,
  coverage_percent REAL,
  FOREIGN KEY (iso3) REFERENCES dim_country(iso3)
);
CREATE INDEX IF NOT EXISTS idx_cov_iso3_year_antigen ON fact_coverage(iso3, year, antigen);

-- Incidence rate (per country-year-disease)
CREATE TABLE IF NOT EXISTS fact_incidence (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  iso3 TEXT,
  country_name TEXT,
  year INTEGER,
  disease TEXT,
  disease_desc TEXT,
  denominator TEXT,
  incidence_rate REAL,
  FOREIGN KEY (iso3) REFERENCES dim_country(iso3)
);
CREATE INDEX IF NOT EXISTS idx_inc_iso3_year_disease ON fact_incidence(iso3, year, disease);

-- Reported cases (per country-year-disease)
CREATE TABLE IF NOT EXISTS fact_cases (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  iso3 TEXT,
  country_name TEXT,
  year INTEGER,
  disease TEXT,
  disease_desc TEXT,
  cases REAL,
  FOREIGN KEY (iso3) REFERENCES dim_country(iso3)
);
CREATE INDEX IF NOT EXISTS idx_cases_iso3_year_disease ON fact_cases(iso3, year, disease);

-- Vaccine introduction (per country-antigen)
CREATE TABLE IF NOT EXISTS dim_vaccine_intro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  iso3 TEXT,
  country_name TEXT,
  who_region TEXT,
  antigen TEXT,
  intro_year INTEGER,
  intro_flag INTEGER,
  FOREIGN KEY (iso3) REFERENCES dim_country(iso3)
);
CREATE INDEX IF NOT EXISTS idx_intro_iso3_antigen ON dim_vaccine_intro(iso3, antigen);

-- Vaccine schedule (per country-year-antigen-round)
CREATE TABLE IF NOT EXISTS dim_schedule (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  iso3 TEXT,
  country_name TEXT,
  who_region TEXT,
  year INTEGER,
  antigen_code TEXT,
  antigen_desc TEXT,
  schedule_round TEXT,
  target_pop TEXT,
  target_pop_desc TEXT,
  geoarea TEXT,
  age_admin TEXT,
  source_comment TEXT,
  FOREIGN KEY (iso3) REFERENCES dim_country(iso3)
);
CREATE INDEX IF NOT EXISTS idx_sch_iso3_year_antigencode ON dim_schedule(iso3, year, antigen_code);

-- Helpful view (cov + incidence join heuristic)
CREATE VIEW IF NOT EXISTS vw_cov_incidence AS
SELECT
  fc.iso3, fc.country_name, fc.year,
  fc.antigen, fc.antigen_desc,
  fi.disease, fi.disease_desc,
  fc.coverage_percent,
  fi.incidence_rate
FROM fact_coverage fc
LEFT JOIN fact_incidence fi
  ON fi.iso3 = fc.iso3 AND fi.year = fc.year;
"""

def build_db():
    # remove old DB to ensure clean schema (optional)
    if os.path.exists(DB_PATH):
        print("[INFO] Removing existing DB:", DB_PATH)
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.executescript(SCHEMA)
        conn.commit()
        print("[SUCCESS] Database created at:", DB_PATH)
    finally:
        conn.close()

if __name__ == "__main__":
    build_db()
