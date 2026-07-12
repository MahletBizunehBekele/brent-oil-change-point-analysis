# Brent Oil Change Point Analysis

## Project Overview

This project analyzes historical Brent crude oil prices to identify significant structural changes using Bayesian Change Point Analysis. The goal is to investigate whether major geopolitical events, OPEC policy decisions, and global economic shocks coincide with significant changes in oil price behavior.

The project is completed as part of the Birhan Energies Change Point Analysis Challenge.

---

## Objectives

The main objectives are to:

- Analyze historical Brent crude oil prices.
- Perform exploratory time series analysis.
- Investigate trend, stationarity, and volatility.
- Build a Bayesian Change Point model using PyMC.
- Detect structural breaks in oil prices.
- Compare detected change points with major historical events.
- Generate data-driven insights for investors, policymakers, and energy companies.

---

## Repository Structure

```
brent-oil-change-point-analysis/
│
├── data/
│   ├── brent_oil_prices.csv
│   └── events.csv
│
├── docs/
│   ├── workflow.md
│   └── assumptions.md
│
├── notebooks/
│   ├── __init__.py
│   └── 01_eda.ipynb
│
├── scripts/
│   └── __init__.py
│
├── src/
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset

### Brent Oil Prices

The primary dataset contains daily Brent crude oil prices from **20 May 1987** to **30 September 2022**.

Columns:

- **Date** – Observation date
- **Price** – Brent crude oil price (USD per barrel)

### Historical Events

A second dataset contains important geopolitical events, OPEC decisions, and global economic events that may have influenced oil prices.

---

## Methodology

The project follows the following workflow:

1. Load historical Brent oil price data.
2. Clean and preprocess the dataset.
3. Perform exploratory data analysis.
4. Study trend, stationarity, and volatility.
5. Build a Bayesian Change Point model.
6. Detect structural breaks.
7. Compare detected change points with historical events.
8. Generate insights and communicate findings.

---

## Exploratory Data Analysis

The exploratory analysis includes:

- Dataset inspection
- Missing value analysis
- Historical price visualization
- Daily log return calculation
- Log return visualization
- Investigation of trend
- Investigation of stationarity
- Investigation of volatility

These analyses provide an understanding of the data before statistical modeling.

---

## Bayesian Change Point Analysis

Bayesian Change Point Analysis is used to identify points in time where the statistical properties of Brent oil prices change significantly.

The model estimates:

- Most probable change point date
- Mean price before the change
- Mean price after the change
- Posterior uncertainty of model parameters

The detected change points are later compared with historical geopolitical and economic events.

---

## Assumptions

Key assumptions include:

- Brent oil prices reflect global market behavior.
- Historical event dates are approximate.
- Markets may react before or after official announcements.
- Daily prices adequately represent market movements.

---

## Limitations

This analysis has several limitations:

- Correlation does not imply causation.
- Multiple global events may occur simultaneously.
- Other macroeconomic variables are not included.
- Bayesian models identify structural changes but cannot prove the exact cause of those changes.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd brent-oil-change-point-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

## Required Libraries

Major Python libraries used include:

- pandas
- numpy
- matplotlib
- scipy
- statsmodels
- pymc
- arviz

---

## Expected Results

The completed project will produce:

- Historical Brent oil price visualizations.
- Daily log return analysis.
- Bayesian change point detection.
- Structural break identification.
- Comparison with major geopolitical and economic events.
- Interactive dashboard for stakeholder exploration.

---

## License

This project is developed for educational purposes as part of the Birhan Energies Change Point Analysis Challenge in KAIM(Kifiya AI mastery program 9).