<h1 align="center" style="color:#2b7a78;">Time-Series Forecasting of Wine Sales – ABC Estate Wines</h1>
<h3 align="center" style="color:#17252a;">Forecasting Monthly Rose & Sparkling Wine Sales Using ARIMA, Holt-Winters, and Moving Averages</h3>

<p align="center">
  <strong>Author:</strong> <a href="https://github.com/nabankur14" target="_blank" style="color:#3aafa9;">Nabankur Ray</a>
</p>

<hr>

<h2 style="color:#17252a;">Overview</h2>
<p>
This project applies <strong>Time-Series Forecasting</strong> and <strong>Statistical Modeling</strong> to predict monthly sales of <strong>Rose</strong> and <strong>Sparkling</strong> wines for <strong>ABC Estate Wines</strong> between <em>January 1980 – November 1995</em>. 
The goal is to understand sales trends, identify seasonality patterns, and generate accurate forecasts to aid in <strong>inventory management</strong>, <strong>marketing strategy</strong>, and <strong>revenue optimization</strong>. 
Comprehensive <em>EDA</em>, <em>model evaluation</em>, and <em>business insight generation</em> were performed to support data-driven decision-making.
</p>

<details open>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Objective</summary>
  <ul>
    <li>Forecast monthly sales for Rose and Sparkling wines using various time-series models.</li>
    <li>Compare the performance of models such as Moving Averages, Holt-Winters, and ARIMA.</li>
    <li>Analyze sales seasonality, trend patterns, and cyclical fluctuations.</li>
    <li>Provide actionable business recommendations for production, inventory, and promotions.</li>
    <li>Evaluate models using RMSE to select the best performing approach.</li>
  </ul>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Dataset</summary>
  <ul>
    <li><strong>Source:</strong> Historical sales data from ABC Estate Wines.</li>
    <li><strong>Period Covered:</strong> January 1980 – November 1995.</li>
    <li><strong>Variables:</strong>
      <ul>
        <li><code>YearMonth</code> – Monthly date index</li>
        <li><code>Rose</code> – Monthly Rose wine sales (units)</li>
        <li><code>Sparkling</code> – Monthly Sparkling wine sales (units)</li>
      </ul>
    </li>
    <li><strong>Data Cleaning:</strong> Missing values in Rose series imputed using mean. Sparkling dataset had no missing data.</li>
    <li><strong>Data Split:</strong> Train set (1980–1992) and Test set (1993–1995) for model validation.</li>
  </ul>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Methodology</summary>
  <ol>
    <li><strong>Data Preprocessing:</strong> 
      <ul>
        <li>Converted <code>YearMonth</code> column to datetime index.</li>
        <li>Handled missing values in the Rose dataset using mean imputation.</li>
      </ul>
    </li>
    <li><strong>Exploratory Data Analysis (EDA):</strong> 
      <ul>
        <li>Visualized trends, seasonality, and noise using line plots and decompositions.</li>
        <li>Identified seasonal peaks and yearly fluctuations in sales.</li>
      </ul>
    </li>
    <li><strong>Model Development:</strong> 
      <ul>
        <li>Baseline Models: Linear Regression, Moving Averages (2, 4, 6, 9 points).</li>
        <li>Smoothing Models: Simple Exponential Smoothing, Holt’s (Double), Holt-Winters (Triple).</li>
        <li>Statistical Models: ARIMA and Auto-ARIMA for optimized parameter selection.</li>
      </ul>
    </li>
    <li><strong>Evaluation Metrics:</strong> Root Mean Square Error (RMSE) for model comparison.</li>
  </ol>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Tools & Technologies</summary>
  <p>
  <code>Python</code>, <code>Pandas</code>, <code>NumPy</code>, <code>Matplotlib</code>, 
  <code>Seaborn</code>, <code>Statsmodels</code>, <code>pmdarima</code>, <code>Scikit-learn</code>, <code>Jupyter Notebook</code>
  </p>
</details>

<details open>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Results & Insights</summary>
  <ul>
    <li><strong>Rose Dataset:</strong> The <code>2-point Trailing Moving Average</code> model achieved the lowest RMSE (~128.19).</li>
    <li><strong>Sparkling Dataset:</strong> The <code>2-point Trailing Moving Average</code> also performed best (RMSE ≈ 7.45×10<sup>5</sup>).</li>
    <li><strong>Seasonality:</strong> Both series displayed clear yearly seasonality patterns, reflecting demand fluctuations.</li>
    <li><strong>Business Insights:</strong> 
      <ul>
        <li>Peak sales months can guide targeted promotional campaigns.</li>
        <li>Inventory levels should align with seasonal forecasts to reduce overstocking.</li>
        <li>Simple models like Moving Averages may outperform complex models when data has stable seasonal patterns.</li>
      </ul>
    </li>
  </ul>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Future Scope</summary>
  <ul>
    <li>Extend forecasting to additional wine categories (Red, White, etc.).</li>
    <li>Deploy the model using <strong>Streamlit</strong> for interactive sales prediction dashboards.</li>
    <li>Incorporate external variables (marketing spend, events, weather) for multivariate forecasting.</li>
    <li>Use advanced models (SARIMA, Prophet, LSTM) for long-term forecasts.</li>
  </ul>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Key Learnings</summary>
  <ul>
    <li>Gained expertise in <strong>time-series decomposition</strong>, <strong>stationarity testing (ADF)</strong>, and <strong>model comparison</strong>.</li>
    <li>Learned the importance of model interpretability in business decision-making.</li>
    <li>Understood how to link statistical forecasting with actionable business insights.</li>
    <li>Enhanced proficiency in Python’s <code>statsmodels</code> and <code>pmdarima</code> libraries.</li>
  </ul>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Folder Structure</summary>
  <pre style="background:#f0f0f0; padding:10px; border-radius:8px;">
  wine_sales_forecasting_project/
  │
  ├── Rose_Sales_Data.csv                         → Monthly Rose wine sales data
  ├── Sparkling_Sales_Data.csv                    → Monthly Sparkling wine sales data
  ├── Nabankur_TSF_Coded_Project.ipynb            → Main Jupyter Notebook (EDA + Modeling)
  ├── BUSINESS_REPORT_TSF_Coded_Project.pdf       → Full analytical & business report
  └── README.md                                   → Project documentation (this file)
  </pre>
</details>

<p align="center" style="color:#555;">
>>> All project files are organized and accessible for easy reproducibility and reference.
</p>

<h2 style="color:#17252a;">#Tags</h2>
<p>
#TimeSeriesForecasting #DataScience #EDA #ARIMA #HoltWinters #MovingAverage #Python #BusinessAnalytics #SalesForecasting #PredictiveModeling #InventoryOptimization
</p>

<hr>
<p align="center" style="font-size:14px; color:#555;">
© 2025 <strong>Nabankur Ray</strong> | Data Scientist
</p>
