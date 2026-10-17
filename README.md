# Week 2: Data Cleaning and Preprocessing Strategy for Agribusiness

## Project Overview
This project develops a repeatable data cleaning and preprocessing strategy for a hypothetical agribusiness dataset. The simulated records represent crop observations across states and include crop yield, temperature, rainfall, and input cost. Intentional issues demonstrate missing-value handling, inconsistent category formatting, duplicate rows, invalid values, and potential outliers.

## Objectives
- Identify common data-quality problems in agricultural datasets.
- Define a step-by-step cleaning and preprocessing workflow.
- Demonstrate Python implementation with Pandas, NumPy, and Scikit-learn.
- Explain reproducibility, validation, and responsible handling of outliers.
- Connect data quality to agribusiness decisions.

## Dataset
`data/agribusiness_raw.csv` contains simulated educational records. It is not actual farm or government data.

Fields include:
- `record_id`: record identifier
- `state`: state/region
- `crop`: crop type
- `observation_date`: date of observation
- `yield_kg_per_acre`: crop yield
- `temperature_c`: temperature in Celsius
- `rainfall_mm`: rainfall in millimetres
- `input_cost_inr_per_acre`: input cost in INR per acre

## Workflow
1. Preserve the original raw file and record its source/version.
2. Inspect shape, types, missingness, and summary statistics.
3. Standardize column names, category labels, and date formats.
4. Convert numeric fields and flag impossible values.
5. Remove confirmed exact duplicates; investigate conflicting IDs.
6. Investigate missing data and record missingness flags.
7. Impute remaining numeric gaps with median for this demonstration.
8. Flag outliers with the IQR rule; do not automatically delete genuine extremes.
9. Save cleaned data with original units.
10. Scale selected numeric features into a separate analysis dataset.
11. Validate outputs and document changes.

## Run the Code
From the repository root:

```bash
pip install -r requirements.txt
python src/preprocess_agribusiness.py
```

The script creates:
- `data/agribusiness_cleaned.csv`
- `data/agribusiness_preprocessed.csv`

## Reproducibility
The raw input is preserved, transformations are documented in code, and outputs can be regenerated. For a real deployment, record extraction date, data owner, schema version, code version, and row counts; use version control and a data-quality log. Fit scalers on training data only when building predictive models to avoid data leakage.

## Example Data-Quality Issues
- Missing temperature or rainfall measurements may result from sensor failures or incomplete field logs.
- `telangana ` differs from `Telangana` because of spacing and capitalization.
- A negative yield is physically invalid and must be investigated.
- A very high rainfall value may be a true weather event or a recording error; verify before changing it.
- Repeated records can inflate crop averages if not identified.

## Agribusiness Use
Reliable data can support crop-yield comparisons, seasonal planning, irrigation review, input-cost monitoring, and resource allocation. Reports should state the date range, number of records, missingness rate, outlier treatment, limitations, and recommended action. Agronomists should validate unusual observations before operational decisions.

## Limitations
The dataset is small and simulated. Imputation and scaling are illustrative methods; real agricultural projects should consider crop, soil type, location, season, measurement units, and domain expertise before selecting final treatments.
