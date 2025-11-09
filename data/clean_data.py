# clean_data.py
import pandas as pd
import os

# Paths
RAW = "data_raw"
EXPORT = "exports"
os.makedirs(EXPORT, exist_ok=True)

# Load dim_country (already prepared WHO master CSV)
df_country = pd.read_csv(os.path.join(RAW, "dim_country.csv"))

# ========== FACT COVERAGE ==========
df_cov = pd.read_excel(os.path.join(RAW, "coverage-data.xlsx"))
df_cov = df_cov.rename(columns={
    "GROUP": "iso3",
    "CODE": "country_code",
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
df_cov = df_cov.merge(df_country[["iso3","country_name","who_region"]],
                      on="iso3", how="left")
df_cov.to_csv(os.path.join(EXPORT, "fact_coverage.csv"), index=False)

# ========== FACT CASES ==========
df_cases = pd.read_excel(os.path.join(RAW, "reported-cases-data.xlsx"))
df_cases = df_cases.rename(columns={
    "GROUP": "iso3",
    "CODE": "country_code",
    "NAME": "country_name",
    "YEAR": "year",
    "DISEASE": "disease",
    "DISEASE_DESCRIPTION": "disease_desc",
    "CASES": "cases"
})
df_cases = df_cases.merge(df_country[["iso3","country_name","who_region"]],
                          on="iso3", how="left")
df_cases.to_csv(os.path.join(EXPORT, "fact_cases.csv"), index=False)

# ========== FACT INCIDENCE ==========
df_inc = pd.read_excel(os.path.join(RAW, "incidence-rate-data.xlsx"))
df_inc = df_inc.rename(columns={
    "GROUP": "iso3",
    "CODE": "country_code",
    "NAME": "country_name",
    "YEAR": "year",
    "DISEASE": "disease",
    "DISEASE_DESCRIPTION": "disease_desc",
    "DENOMINATOR": "denominator",
    "INCIDENCE_RATE": "incidence_rate"
})
df_inc = df_inc.merge(df_country[["iso3","country_name","who_region"]],
                      on="iso3", how="left")
df_inc.to_csv(os.path.join(EXPORT, "fact_incidence.csv"), index=False)

# ========== DIM SCHEDULE ==========
df_sch = pd.read_excel(os.path.join(RAW, "vaccine-schedule-data.xlsx"))
df_sch = df_sch.rename(columns={
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
df_sch.to_csv(os.path.join(EXPORT, "dim_schedule.csv"), index=False)

# ========== DIM VACCINE INTRO ==========
df_intro = pd.read_excel(os.path.join(RAW, "vaccine-introduction-data.xlsx"))
df_intro = df_intro.rename(columns={
    "ISO_3_CODE": "iso3",
    "COUNTRYNAME": "country_name",
    "WHO_REGION": "who_region",
    "YEAR": "intro_year",
    "DESCRIPTION": "antigen",
    "INTRO": "intro_flag"
})
df_intro.to_csv(os.path.join(EXPORT, "dim_vaccine_intro.csv"), index=False)

print("✅ All clean CSVs exported to 'exports/' folder")
