# Time Series Wine Sales Forecasting

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **A comprehensive time series forecasting project analyzing historical sales data to predict future demand for Rose and Sparkling wines at ABC Estate Wines.**

This project leverages historical sales data from ABC Estate Wines to predict future demand for Rose and Sparkling wines. By applying advanced time series forecasting techniques (ARIMA, Holt-Winters), we provide actionable insights to drive data-informed decision-making.


---

## Table of Contents
- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Key Results](#key-results)
- [Business Impact](#business-impact)
- [Skills](#skills)
- [Key Learnings](#key-learnings)
- [Future Improvements](#future-improvements)
- [Repository Structure](#repository-structure)
- [Author](#-author)

---

## Project Overview

This project focuses on leveraging data analytics and advanced forecasting techniques to uncover hidden sales patterns, detect seasonal trends, and predict the future demand for distinct wine varieties (Rose and Sparkling). By thoroughly analyzing 20th-century historical sales data, this project develops predictive models that serve as a foundational tool for inventory planning, marketing optimization, and strategic decision-making.

👉 [Open the rose wine notebook to explore full analysis](notebooks/rose_wines.ipynb)

👉 [Open the sparkling wine notebook to explore full analysis](notebooks/sparkling_wines.ipynb)

---

## Business Problem

**Real-World Context:** ABC Estate Wines has collected extensive historical sales records for different types of wines spanning from 1980 to 1995. While overall growth is steady, the varying seasonal peaks and periodic fluctuations between wine types make supply chain management and marketing resource allocation challenging.

**Stakeholders:** ABC Estate Wines Management, Supply Chain Planners, and the Marketing & Strategy Teams.

**Decision Impact:** Accurate demand forecasting equips stakeholders with the necessary foresight to align inventory with expected demand, preventing costly stockouts during peak seasons and minimizing holding costs during low-demand months. It also enables highly targeted promotional campaigns, maximizing revenue and maintaining a competitive edge in the wine industry.

---

## Dataset

**Source:** Provided as part of PGP-DSBA project (ABC Estate Wines).

**Size:** 187 records per dataset, encompassing monthly data from January 1980 to November 1995.

**Key Features:**

* YearMonth: Represents the year and month of the sales data (YYYY-MM format).

* Rose: Monthly sales volume of Rose wine.

* Sparkling: Monthly sales volume of Sparkling wine.

* Data Types: YearMonth (Object/Datetime), Rose (Float64), Sparkling (Int64).

---

## Methodology

The methodology strictly follows a professional data science lifecycle, tailored specifically for Time Series Forecasting:

1. **Understanding the Data**: Inspected the data structure, data types, dimensions, and performed statistical summaries to understand mean variations, ranges, and potential anomalies.

2. **Exploratory Data Analysis (EDA)**: Conducted univariate analysis to map long-term trends and seasonality. Deployed Additive and Multiplicative Decomposition to break the time series down into distinct observed, trend, seasonal, and residual components.

3. **Data Pre Processing**: Handled missing values (mean imputation for the Rose dataset), converted YearMonth into DateTime format, and chronologically split the data into a Training set (1980–1992) and a Test set (1993 onwards).

4. **Model Building - Original Data**: Regressed the data against time using Linear Regression. Implemented Trailing Moving Averages (2, 4, 6, and 9 points) and advanced smoothing techniques including Simple Exponential Smoothing, Double Exponential Smoothing (Holt's Model), and Triple Exponential Smoothing (Holt-Winter's Model).

5. **Checking for Stationary**: Verified series stationarity utilizing rolling means, standard deviations, and the augmented Dickey-Fuller Test.

6. **Model Building - Stationary Data**: Applied autoregressive modeling techniques including ARIMA, Auto ARIMA, and SARIMAX.

7. **Evaluation**: Benchmarked the predictive performance of all models on the test dataset utilizing Root Mean Squared Error (RMSE) to deduce the highest-accuracy solution.

---

## Key Results

**Main Metrics**: Root Mean Squared Error (RMSE) was utilized as the primary evaluation metric.

**Model Performance**: The 2-point Trailing Moving Average emerged as the superior model for both datasets, achieving the lowest RMSE (128.19 for Rose, and 745,291.6 for Sparkling). Triple Exponential Smoothing was the second-best performer, effectively handling seasonality. Linear Regression and Double Exponential Smoothing struggled significantly to capture the complex temporal patterns.

**Key Insights**: * Sparkling wine demonstrated substantially higher overall sales volumes, sharper fluctuations, and a proportionally increasing long-term trend.

    Rose wine exhibited a gradual, steady long-term decline in sales volume.

    Both datasets showcased strong, recurring, and highly periodic seasonal components linked to specific times of the year, likely driven by holidays and celebrations.

---

## Business Impact

* Introduce targeted promotional discounts and bundled product offers during identified high-demand seasonal peaks to aggressively maximize revenue.

* Align strict inventory planning with forecasted seasonal demand to successfully prevent stockouts during peak holiday periods, while minimizing holding/storage costs during off-peak seasons.

* Explore the introduction of new wine variants or complementary products to capitalize on observed consistent growth trends (especially in the Sparkling sector).

* Focus heavily on digital marketing and social media campaigns aimed at younger demographics to proactively reverse the long-term sales decline observed in the Rose wine category.

* Real-world value: This end-to-end forecasting pipeline empowers the business to transition from reactive operations to a highly proactive, data-driven strategy, optimizing the entire supply chain footprint and enhancing the ROI of marketing expenditures.

---

## Skills

**Technical:**
*   **Programming & Tools:** Python, Jupyter Notebooks
*   **Data Manipulation & Analysis:** pandas, numpy, exploratory-data-analysis, trend-analysis
*   **Machine Learning & Statistics:** scikit-learn, statsmodels
*   **Forecasting & Modeling:** time-series-forecasting, demand-forecasting, arima, sarimax, exponential-smoothing
*   **Visualization:** matplotlib, seaborn
*   **Business Applications:** inventory-optimization

**Soft:**
*   **Data Storytelling:** Translating complex technical output (e.g., RMSE, Model parameters) into clear, actionable business narratives.
*   **Cross-Functional Communication:** Bridging the gap between the analytics lifecycle and non-technical stakeholders (Supply Chain Planners, Marketing Teams).
*   **Strategic Business Acumen:** Aligning predictive modeling metrics with operational goals, minimizing holding costs, and maximizing promotional ROI.
*   **Analytical Problem Solving:** Evaluating trade-offs between model complexity and interpretability (e.g., ARIMA vs. Holt-Winters) to deduce the highest-accuracy solution.

---

## Key Learnings

*   The importance of decomposing time series to understand underlying components.
*   Trade-offs between model complexity (ARIMA) and interpretability (Holt-Winters).
*   Translating technical metrics (RMSE) into business terms (Risk/Accuracy).

---

## Future Improvements

1.  **Deploy as Web App**: Create a Streamlit dashboard for real-time forecasting.
2.  **Incorporate Exogenous Variables**: Include marketing spend or weather data to improve accuracy.
3.  **Automate Pipeline**: Set up a CI/CD pipeline for automated monthly re-training.
4.  **Try Deep Learning**: Experiment with LSTM or Prophet models.

---

## Repository Structure
```text
Time_Series_Wine_Sales_Forecasting/
│
├── data/
│   ├── Rose.csv                  # Rose wine dataset
│   └── Sparkling.csv             # Sparkling wine dataset
│   
├── notebooks/
│   ├── rose_wines.ipynb          # Rose wine analysis notebook
│   └── sparkling_wines.ipynb     # Sparkling wine analysis notebook
│
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── LICENSE                       # MIT License
└── README.md                     # Project documentation
```

---

## Author

**Nabankur Ray**

Passionate about real-world data-driven solutions

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github)](https://github.com/nabankur14) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/nabankur-ray-876582181/)

![GitHub Stats](https://github-readme-stats-eight-theta.vercel.app/api?username=nabankur14&show_icons=true)

---

⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!