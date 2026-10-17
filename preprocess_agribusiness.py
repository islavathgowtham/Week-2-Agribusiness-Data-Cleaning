"""
Week 2: Agribusiness Data Cleaning and Preprocessing Strategy
Input: data/agribusiness_raw.csv
Outputs: data/agribusiness_cleaned.csv and data/agribusiness_preprocessed.csv

The input is simulated educational data, not actual farm records.
"""
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

ROOT = Path(__file__).resolve().parents[1]
input_path = ROOT / "data" / "agribusiness_raw.csv"
clean_path = ROOT / "data" / "agribusiness_cleaned.csv"
processed_path = ROOT / "data" / "agribusiness_preprocessed.csv"

df = pd.read_csv(input_path)
print("Raw shape:", df.shape)
print("Missing values by column:\n", df.isna().sum())

# Standardize field names and categorical strings.
df.columns = df.columns.str.strip().str.lower()
for col in ["record_id", "state", "crop"]:
    df[col] = df[col].astype("string").str.strip()
df["state"] = df["state"].str.title()
df["crop"] = df["crop"].str.title()
df["observation_date"] = pd.to_datetime(df["observation_date"], errors="coerce")

numeric_cols = [
    "yield_kg_per_acre", "temperature_c", "rainfall_mm",
    "input_cost_inr_per_acre"
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove exact duplicate rows. In production, conflicting IDs must be investigated.
before = len(df)
df = df.drop_duplicates()
print("Exact duplicate rows removed:", before - len(df))

# Flag impossible values; replace them with missing values for review.
invalid_yield = df["yield_kg_per_acre"] < 0
df["yield_invalid_flag"] = invalid_yield.astype(int)
df.loc[invalid_yield, "yield_kg_per_acre"] = np.nan

invalid_rain = df["rainfall_mm"] < 0
df["rainfall_invalid_flag"] = invalid_rain.astype(int)
df.loc[invalid_rain, "rainfall_mm"] = np.nan

# Record missingness before imputation.
for col in numeric_cols:
    df[col + "_was_missing"] = df[col].isna().astype(int)

# Use median imputation as a simple demonstration.
# A real project should first check field books/sensors and consider crop/region/season groups.
for col in numeric_cols:
    if df[col].isna().any():
        df[col] = df[col].fillna(df[col].median())

# Detect potential outliers with the IQR rule; do not delete automatically.
for col in ["yield_kg_per_acre", "temperature_c", "rainfall_mm", "input_cost_inr_per_acre"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df[col + "_outlier_flag"] = ((df[col] < low) | (df[col] > high)).astype(int)

# Save a cleaned copy with original measurement units retained.
df.to_csv(clean_path, index=False)

# Normalize selected numeric features in a separate analysis copy.
processed = df.copy()
scale_cols = ["yield_kg_per_acre", "temperature_c", "rainfall_mm", "input_cost_inr_per_acre"]
scaler = MinMaxScaler()
processed[[c + "_scaled" for c in scale_cols]] = scaler.fit_transform(processed[scale_cols])
processed.to_csv(processed_path, index=False)

print("Cleaned shape:", df.shape)
print("Cleaned file:", clean_path)
print("Preprocessed file:", processed_path)
print("Note: for predictive modelling, fit the scaler on training data only.")
