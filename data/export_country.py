import sqlite3
import pandas as pd
import os

# Paths
BASE = r"C:\JN\Vaccination-Project"   # <-- अपने project folder का सही path डालें
DB_PATH = os.path.join(BASE, "data", "vaccination.db")
EXPORT_PATH = os.path.join(BASE, "exports", "dim_country.csv")

# Step 1: Connect DB
conn = sqlite3.connect(DB_PATH)

# Step 2: Query unique countries
query = """
SELECT DISTINCT f.iso3,
       c.country_name,
       c.who_region
FROM fact_coverage f
LEFT JOIN dim_country c
       ON f.iso3 = c.iso3
WHERE f.iso3 IS NOT NULL
ORDER BY f.iso3;
"""

df_country = pd.read_sql(query, conn)

# Step 3: If country_name or who_region missing, mark as 'Unknown'
df_country["country_name"].fillna("Unknown", inplace=True)
df_country["who_region"].fillna("Unknown", inplace=True)

# Step 4: Export to CSV
os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)
df_country.to_csv(EXPORT_PATH, index=False)

print(f"[SUCCESS] dim_country.csv recreated → {EXPORT_PATH}")
print(f"Total countries exported: {len(df_country)}")

conn.close()
