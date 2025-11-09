-- Countries & Regions (normalized)
CREATE TABLE IF NOT EXISTS dim_country (
  iso3 TEXT PRIMARY KEY,
  country_name TEXT,
  who_region TEXT
);

-- Coverage (per country-year-antigen-dose/category)
CREATE TABLE IF NOT EXISTS fact_coverage (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  iso3 TEXT,
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
  antigen TEXT,            -- 'Description' से normalized
  intro_year INTEGER,      -- Intro = yes वाले में Year
  intro_flag INTEGER,      -- 1/0 (yes/no)
  FOREIGN KEY (iso3) REFERENCES dim_country(iso3)
);
CREATE INDEX IF NOT EXISTS idx_intro_iso3_antigen ON dim_vaccine_intro(iso3, antigen);

-- Vaccine schedule (per country-year-antigen-round)
CREATE TABLE IF NOT EXISTS dim_schedule (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  iso3 TEXT,
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
