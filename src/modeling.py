
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression

def decompose_series(series, model='additive', period=12):
    """
    Decomposes a time series.
    
    Args:
        series (pd.Series): The time series data.
        model (str): Type of decomposition ('additive' or 'multiplicative').
        period (int): The period of the series.
        
    Returns:
        DecomposeResult: The decomposition result.
    """
    return seasonal_decompose(series, model=model, period=period)

def fit_arima(series, order):
    """
    Fits an ARIMA model to the series.
    
    Args:
        series (pd.Series): The time series data.
        order (tuple): The (p,d,q) order of the ARIMA model.
        
    Returns:
        ARIMAResultsWrapper: The fitted ARIMA model.
    """
    model = ARIMA(series, order=order)
    return model.fit()

def fit_holt_winters(series, seasonal_periods=12, trend='add', seasonal='add'):
    """
    Fits a Holt-Winters Exponential Smoothing model.
    
    Args:
        series (pd.Series): The time series data.
        seasonal_periods (int): The number of periods in a season.
        trend (str): Type of trend component.
        seasonal (str): Type of seasonal component.
        
    Returns:
        HoltWintersResultsWrapper: The fitted model.
    """
    model = ExponentialSmoothing(series, seasonal_periods=seasonal_periods, trend=trend, seasonal=seasonal)
    return model.fit()
