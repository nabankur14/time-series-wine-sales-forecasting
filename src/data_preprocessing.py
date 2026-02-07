
import pandas as pd
import numpy as np

def load_data(filepath, date_col='YearMonth', format='%Y-%m'):
    """
    Loads time series data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        date_col (str): Name of the date column.
        format (str): Date format string.
        
    Returns:
        pd.DataFrame: Loaded dataframe with datetime index.
    """
    try:
        data = pd.read_csv(filepath)
        data[date_col] = pd.to_datetime(data[date_col], format=format)
        data.set_index(date_col, inplace=True)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def check_missing_values(data):
    """
    Checks for missing values in the dataframe.
    
    Args:
        data (pd.DataFrame): The dataframe to check.
        
    Returns:
        pd.Series: Count of missing values per column.
    """
    return data.isnull().sum()
