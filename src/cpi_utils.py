import pandas as pd
from pandas_datareader import DataReader
from datetime import datetime

def fetch_cpi_data():
    """
    Fetches CPI data from FRED and returns a DataFrame.
    """
    start_date = datetime(datetime.now().year - 2, 1, 1)  # Fetch data from 2 years ago
    end_date = datetime.now()

    # Fetch CPI data using the FRED API
    cpi_data = DataReader('CPIAUCSL', 'fred', start_date, end_date)

    return cpi_data

def calculate_quarterly_inflation(cpi_data):
    """
    Calculates quarterly inflation from CPI data.

    Args:
        cpi_data (pd.DataFrame): DataFrame with CPI data.

    Returns:
        pd.Series: Quarterly inflation rates(index: year + quarter).
    """
    # mark season of each row
    cpi_data = cpi_data.reset_index()
    cpi_data['DATE'] = pd.to_datetime(cpi_data['DATE'])
    cpi_data['Quarter'] = cpi_data['DATE'].dt.to_period('Q')
    
    # Extract the last month's CPI for each quarter
    quarterly_cpi = cpi_data.groupby('Quarter').last().reset_index()

    # Calculate the quarterly inflation rate
    quarterly_cpi['Quarterly Inflation'] = quarterly_cpi['CPIAUCSL'].pct_change() * 100

    # Convert `Quarter` column to a categorical type and make it ordinal
    quarterly_cpi['Quarter'] = pd.Categorical(quarterly_cpi['Quarter'], ordered=True)

    # Set `Quarter` as the index
    quarterly_cpi = quarterly_cpi.set_index('Quarter')

    # Get the last 4 quarters
    last_4_quarters = quarterly_cpi['Quarterly Inflation'].dropna().iloc[-4:]

    return last_4_quarters