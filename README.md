# Time Series Wine Sales Forecasting 🍷📈

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 🌟 Hero Section

**Forecasting the future of wine sales to optimize inventory and marketing strategies for the 20th century.**

This project leverages historical sales data from ABC Estate Wines to predict future demand for Rose and Sparkling wines. By applying advanced time series forecasting techniques (ARIMA, Holt-Winters), we provide actionable insights to drive data-informed decision-making.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [Key Results](#-key-results)
- [Business Impact](#-business-impact)
- [Repo Structure](#-repository-structure)
- [How to Run](#-how-to-run)
- [Author](#-author)

---

## 🚀 Project Overview
**What:** A comprehensive time series analysis and forecasting project for Rose and Sparkling wine sales.
**Why:** To understand historical sales patterns and provide accurate future sales estimates, enabling better resource allocation and strategic planning.

## 💼 Business Problem
**Problem:** ABC Estate Wines faces uncertainty in future demand, leading to potential stockouts or overstocking issues.
**Stakeholders:** Inventory Managers, Sales Directors, Marketing Team.
**Decision Impact:** Accurate forecasts will directly influence production schedules, inventory costs, and targeted marketing campaigns.

## 📊 Dataset
**Source:** ABC Estate Wines Internal Historical Data.
**Size:** Monthly sales data spanning the 20th century.
**Key Features:** `YearMonth` (Time Index), `Rose` (Sales Volume), `Sparkling` (Sales Volume).
**Data Types:** Time Series Data.

## 🛠️ Methodology
1.  **Data Cleaning**: Handled missing values, parsed dates, and set time-based indices.
2.  **Exploratory Data Analysis (EDA)**: Decomposed series into Trend, Seasonality, and Residual components. Visualized sales distribution and monthly patterns.
3.  **Model Building**:
    *   **Rose Wine**: Applied ARIMA and Holt-Winters Exponential Smoothing.
    *   **Sparkling Wine**: Investigated seasonality and trend components for appropriate model selection.
4.  **Evaluation**: Models were evaluated using **RMSE** (Root Mean Squared Error) to ensure forecast accuracy.

## 📈 Key Results
*   **Seasonality**: Both wine types exhibit strong seasonal patterns, likely driven by holidays and weather seasons.
*   **Trend**: Identifying long-term growth or decline trends to adjust strategic focus.
*   **Performance**: The selected models successfully capture the underlying patterns, providing reliable short-term forecasts.

## 💡 Business Impact
1.  **Inventory Optimization**: Align stock levels with seasonal peaks to reduce holding costs and lost sales.
2.  **Marketing Timing**: Launch campaigns ahead of predicted high-demand periods.
3.  **Production Planning**: Adjust production schedules based on long-term trend forecasts.

## 🧠 Skills
**Technical:**
*   Python (Pandas, NumPy, Scikit-learn, Statsmodels)
*   Time Series Analysis (ARIMA, Exponential Smoothing)
*   Data Visualization (Matplotlib, Seaborn)
*   Jupyter Notebooks

**Soft:**
*   Data Storytelling
*   Strategic Thinking
*   Business Reporting

## 🔑 Key Learnings
*   The importance of decomposing time series to understand underlying components.
*   Trade-offs between model complexity (ARIMA) and interpretability (Holt-Winters).
*   Translating technical metrics (RMSE) into business terms (Risk/Accuracy).

## 📂 Repository Structure
```
project-name/
├── data/
│   ├── raw/          # Original datasets
│   └── processed/    # Cleaned data
├── notebooks/        # Jupyter analysis notebooks
├── src/              # Source code modules
│   ├── data_preprocessing.py
│   ├── modeling.py
│   └── evaluation.py
├── reports/          # PDF business reports
├── visuals/          # Generated charts
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

## 💻 How to Run
```bash
# 1. Clone the repository
git clone <repo-url>
cd time-series-wine-sales-forecasting

# 2. Install dependencies
pip install -r requirements.txt

# 3. Explore the notebooks
jupyter notebook notebooks/rose_wines.ipynb
```

## 🔮 Future Improvements
1.  **Deploy as Web App**: Create a Streamlit dashboard for real-time forecasting.
2.  **Incorporate Exogenous Variables**: Include marketing spend or weather data to improve accuracy.
3.  **Automate Pipeline**: Set up a CI/CD pipeline for automated monthly re-training.
4.  **Try Deep Learning**: Experiment with LSTM or Prophet models.

## ✍️ Author
**Nabankur Ray**
*   **Role**: Data Scientist
*   [GitHub Profile](https://github.com/nabankur14)
*   [LinkedIn Profile](https://linkedin.com/in/nabankur14)
