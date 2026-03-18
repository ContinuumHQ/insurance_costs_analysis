# US Medical Insurance Costs Analysis

> Baseline project — one of my first Python scripts, built during the Codecademy
> Data Scientist certification. Intentionally unrefactored.
> The contrast to [hiring-gap-analysis](https://github.com/ContinuumHQ/hiring-gap-analysis)
> tells the learning curve better than any CV.

---

## Project Goals

Independent exploratory data analysis (EDA) of the US Medical Insurance Costs dataset,
identifying the key predictors of medical charges.

Questions explored:

1. **Smoking impact:** What is the average cost difference between smokers and non-smokers?
2. **Regional differences:** Are there significant cost variations across the four US regions?
3. **Physical factors:** How do age and BMI combined with number of children affect individual charges?

---

## Dataset Overview

The dataset (`insurance.csv`) contains 7 columns:

| Column   | Description                                      | Type              |
|----------|--------------------------------------------------|-------------------|
| age      | Age of the primary beneficiary                   | Numeric (Integer) |
| sex      | Gender of the policyholder                       | Categorical       |
| bmi      | Body Mass Index                                  | Numeric (Float)   |
| children | Number of children covered by the plan           | Numeric (Integer) |
| smoker   | Smoking status                                   | Categorical       |
| region   | Residential region in the US (4 regions)         | Categorical       |
| charges  | Individual medical costs billed by insurance     | Numeric (Float)   |

---

## Methodology

1. Data import via Python `csv` library into a list of dictionaries
2. Type conversion and basic cleaning
3. Functions for averages, frequencies and correlations
4. Results summarized in the notebook

### Visualizations

- Bar chart: average charges by region — Southeast consistently highest

---

## Note on this repository

This documents my starting point in data analysis with Python. Code is left in its
original state, including minor library warnings, to authentically reflect the
learning curve.

To see how I write clean, production-grade code today, check out:
- [hiring-gap-analysis](https://github.com/ContinuumHQ/hiring-gap-analysis) — live ETL pipeline, ML forecasting, Docker
- [portfolio](https://github.com/ContinuumHQ/portfolio) — 3 production-ready projects with tests and docs
