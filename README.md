# Week 2 Task: Data Cleaning and Preprocessing Strategy for Agribusiness

## 1. Project Overview

This project focuses on developing a systematic data cleaning and preprocessing strategy for a hypothetical agribusiness dataset. The primary objective is to identify common data quality issues and prepare agricultural data for reliable analysis and decision-making.

Agricultural datasets often contain missing measurements, inconsistent formats, duplicate records, invalid values, and outliers. These issues can affect crop yield analysis, weather assessment, input cost estimation, seasonal planning, and agricultural forecasting. This project demonstrates how these problems can be identified and addressed using Python-based data preprocessing techniques.

The project uses a simulated agricultural dataset containing crop information, state, observation date, crop yield, temperature, rainfall, and input cost. The dataset is designed for educational purposes and includes example data quality issues to demonstrate the proposed workflow.

## 2. Project Objectives

- Identify common data quality issues in agribusiness datasets.
- Develop a step-by-step data cleaning strategy.
- Handle missing values using appropriate imputation techniques.
- Standardize inconsistent categorical values and date formats.
- Identify and remove confirmed duplicate records.
- Validate numerical values and detect potential outliers.
- Apply normalization techniques to selected numerical features.
- Explain the importance of reproducibility in data preprocessing.
- Demonstrate how clean data supports agricultural analysis and planning.

## 3. Technologies Used

- **Python:** Implementation of the preprocessing workflow.
- **Pandas:** Data loading, exploration, cleaning, and manipulation.
- **NumPy:** Numerical operations and invalid-value handling.
- **Scikit-learn:** Min-Max normalization.
- **CSV:** Storage of raw and processed datasets.
- **GitHub:** Version control and project documentation.

## 4. Dataset Description

The simulated dataset contains the following attributes:

| Column | Description |
|---|---|
| record_id | Unique identifier for each observation |
| state | State or agricultural region |
| crop | Type of crop |
| observation_date | Date of observation |
| yield_kg_per_acre | Crop yield in kilograms per acre |
| temperature_c | Temperature in degrees Celsius |
| rainfall_mm | Rainfall in millimetres |
| input_cost_inr_per_acre | Agricultural input cost in INR per acre |

**Note:** The dataset contains hypothetical records and does not represent actual farm data or official agricultural statistics.

## 5. Common Data Quality Issues

### Missing Values
Missing temperature, rainfall, or crop yield measurements can reduce the reliability of agricultural analysis. The strategy checks the original source where possible and demonstrates median imputation for remaining numerical gaps.

### Inconsistent Formats
Differences such as `telangana` and `Telangana` can create separate categories for the same state. Whitespace removal and consistent capitalization help standardize these values.

### Duplicate Records
Repeated records can distort crop averages and record counts. Confirmed duplicate rows are removed, while conflicting identifiers require further investigation.

### Invalid Values
Negative crop yield, rainfall, or input costs may indicate recording or data-entry errors. Such values are flagged and reviewed before analysis.

### Outliers
Unusually high rainfall or crop yield measurements may indicate errors or genuine agricultural events. The Interquartile Range (IQR) method is used to flag unusual observations for investigation rather than automatically deleting them.

## 6. Data Cleaning and Preprocessing Workflow

The project follows these steps:

1. Preserve the original dataset.
2. Inspect the dataset structure, data types, and missing values.
3. Standardize column names and categorical values.
4. Convert dates and numerical columns into appropriate data types.
5. Identify and remove confirmed duplicate rows.
6. Validate numerical values and flag invalid observations.
7. Record missingness and apply suitable imputation methods.
8. Detect potential outliers using the IQR method.
9. Apply Min-Max normalization to selected numerical features.
10. Validate the cleaned dataset and save the processed outputs.
11. Document all transformations for reproducibility.

## 7. Python Implementation

The preprocessing script is available in `src/preprocess_agribusiness.py`.

The implementation uses Pandas, NumPy, and Scikit-learn to perform data cleaning, missing-value handling, duplicate removal, outlier detection, and normalization.

To run the project, install the dependencies:

```bash
pip install -r requirements.txt
```

Execute the preprocessing script from the project root directory:

```bash
python src/preprocess_agribusiness.py
```

The script generates the following files:

- `data/agribusiness_cleaned.csv`
- `data/agribusiness_preprocessed.csv`

The cleaned dataset retains the original measurement units, while the preprocessed dataset includes normalized numerical features.

## 8. Reproducibility

Reproducibility ensures that the same cleaning procedure can be repeated and verified. This project supports reproducibility by preserving the raw dataset, documenting the preprocessing steps in Python, maintaining dependencies in `requirements.txt`, and storing the project in GitHub.

In practical agricultural projects, the data source, collection date, units, transformation rules, code version, and validation results should also be recorded. Original values and outlier flags should be retained for audit and review.

When predictive modelling is performed, imputation and normalization parameters should be fitted using training data only to prevent data leakage.

## 9. Applications in Agribusiness

Reliable agricultural data can support:

- Crop yield comparison across regions.
- Seasonal agricultural planning.
- Rainfall and temperature analysis.
- Irrigation and resource planning.
- Agricultural input cost monitoring.
- Identification of unusual crop observations.
- Data-driven decision-making and future forecasting.

The cleaned data can be summarized in reports and dashboards for agronomists, field officers, farm managers, finance teams, and agricultural analysts.

## 10. Expected Outcomes

The expected outcomes are a documented preprocessing strategy, a reusable Python cleaning script, a cleaned agricultural dataset, a normalized analysis dataset, and a reproducible workflow.

The approach improves data consistency and makes potential data quality issues easier to identify before further analysis. Actual agricultural conclusions should only be drawn after validating the dataset and consulting relevant domain experts.

## 11. Conclusion

This project demonstrates the importance of data cleaning and preprocessing in agribusiness analytics. By addressing missing values, inconsistent formats, duplicate records, invalid measurements, and outliers, agricultural data can be prepared for more reliable analysis.

The use of Python and a documented, reproducible workflow supports transparency, consistency, and future improvements. These techniques can help prepare agricultural datasets for crop analysis, resource planning, business intelligence, and predictive modelling.

## 12. Limitations

- The dataset is simulated for educational purposes.
- Median imputation is a demonstration method and may not suit every agricultural variable.
- Outliers require domain-specific investigation before any correction.
- The workflow should be adapted to the crop, location, season, units, and data collection method of a real project.

## 13. References

- Pandas Documentation: https://pandas.pydata.org/docs/
- NumPy Documentation: https://numpy.org/doc/
- Scikit-learn MinMaxScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
- Food and Agriculture Organization of the United Nations: https://www.fao.org/

---

**Project:** Week 2 – Data Cleaning and Preprocessing Strategy for Agribusiness  
**Purpose:** Academic learning and demonstration of data preprocessing techniques  
**Dataset:** Simulated agricultural data
