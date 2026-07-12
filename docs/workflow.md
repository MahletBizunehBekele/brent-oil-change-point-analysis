# Brent Oil Change Point Analysis Workflow

## Objective

The objective of this project is to analyze historical Brent crude oil prices and identify significant structural changes in price behavior over time. The analysis aims to investigate whether these changes coincide with major geopolitical events, OPEC policy decisions, and global economic shocks. The findings will support investors, policymakers, and energy companies in understanding how global events influence oil market dynamics.

---

# Analysis Workflow

## 1. Data Collection

The analysis begins by collecting the historical Brent crude oil price dataset covering daily prices from May 1987 to September 2022. In addition, a separate dataset containing major geopolitical events, OPEC decisions, and global economic events is compiled to provide contextual information for interpreting detected structural changes.

---

## 2. Data Preparation

The Brent oil price dataset is loaded into Python using Pandas. The Date column is converted into a datetime format, the data is sorted chronologically, and missing values or inconsistencies are checked. This ensures that the dataset is clean and suitable for time series analysis.

---

## 3. Exploratory Data Analysis (EDA)

Exploratory analysis is performed to understand the characteristics of the data before building statistical models. The historical Brent oil price series is visualized to identify long-term trends, major price shocks, and periods of high volatility. Daily log returns are also calculated and plotted because they are generally more appropriate for statistical analysis than raw prices.

---

## 4. Time Series Investigation

Key statistical properties of the time series are examined, including trend, stationarity, and volatility. These properties help determine whether transformations such as log returns are necessary before modeling. Understanding these characteristics is essential because many statistical models assume relatively stable data over time.

---

## 5. Bayesian Change Point Modeling

A Bayesian Change Point model will be developed using PyMC to identify points in time where the statistical behavior of Brent oil prices changes significantly. The model estimates the most probable change point along with parameter values before and after the detected structural break.

---

## 6. Event Comparison

The estimated change points are compared with the compiled dataset of geopolitical events, OPEC policy decisions, and major economic shocks. Events occurring near identified structural breaks are investigated as potential explanations for observed changes in oil price behavior.

---

## 7. Interpretation and Communication

The final stage focuses on interpreting the modeling results and communicating insights to stakeholders. Findings will summarize major structural changes, discuss possible relationships with historical events, quantify changes before and after detected breakpoints, and explain the limitations of the analysis.

---

# Expected Outputs

The analysis is expected to produce:

- Visualizations of historical Brent oil prices and daily log returns.
- Identification of significant structural change points.
- Estimated model parameters before and after each detected change.
- Comparison of detected change points with major geopolitical, OPEC, and economic events.
- Data-driven insights to support investment, policy, and operational decision-making.

---

# Communication Channels

The final results will be communicated through:

- A Jupyter Notebook containing the complete analysis.
- An interactive dashboard for exploring historical prices and detected events.
- Visualizations showing price trends and structural breaks.
- A written report summarizing key findings and business implications.