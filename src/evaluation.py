
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def calculate_rmse(y_true, y_pred):
    """
    Calculates the Root Mean Squared Error.
    
    Args:
        y_true (array-like): True values.
        y_pred (array-like): Predicted values.
        
    Returns:
        float: The RMSE value.
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))

def plot_forecast(train, test, forecast, title="Forecast vs Actuals"):
    """
    Plots the training data, test data, and forecast.
    
    Args:
        train (pd.Series): Training data.
        test (pd.Series): Test data.
        forecast (pd.Series): Forecasted data.
        title (str): Plot title.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train, label='Train')
    plt.plot(test.index, test, label='Test')
    plt.plot(test.index, forecast, label='Forecast')
    plt.title(title)
    plt.legend()
    plt.show()
