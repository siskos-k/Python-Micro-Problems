
import numpy as np
import pandas as pd
from scipy.stats import norm
from matplotlib import pyplot as plt
def generate_stock_history(start_price=100, mean_return=0.05, volatility=0.2, num_days=250):
    """
    Generates a synthetic stock price history for a single stock.

    Parameters:
    start_price (float): The initial stock price.
    mean_return (float): The average daily return on the stock.
    volatility (float): The volatility of the stock returns.
    num_days (int): The number of days in the stock history.

    Returns:
    A pandas DataFrame with the stock price history.
    """
    # Calculate the daily returns based on the mean and volatility
    daily_returns = np.random.normal(loc=mean_return, scale=volatility, size=num_days)

    # Compound the daily returns to get the stock prices for each day
    stock_prices = np.exp(daily_returns).cumprod() * start_price

    # Return the stock price history as a DataFrame
    return pd.DataFrame(stock_prices, index=pd.RangeIndex(start=1, stop=num_days+1))

# Generate a 250-day stock price history
stock_history = generate_stock_history(start_price=100, mean_return=0.05, volatility=0.2, num_days=250)

# # Plot the stock price history
# stock_history.plot()
# plt.show()
def generate_multiple_stock_histories(num_stocks=10, start_price=100, mean_return=0.05, volatility=0.2, num_days=250):
    """
    Generates a dataset of multiple synthetic stock price histories.

    Parameters:
    num_stocks (int): The number of stocks to generate.
    start_price (float): The initial stock price for each stock.
    mean_return (float): The average daily return on the stocks.
    volatility (float): The volatility of the stock returns.
    num_days (int): The number of days in the stock history for each stock.

    Returns:
    A pandas DataFrame with the multi-stock price history.
    """
    # Generate the stock price histories for each stock
    stock_histories = [generate_stock_history(start_price=start_price, mean_return=mean_return, volatility=volatility, num_days=num_days) for _ in range(num_stocks)]

    # Concatenate the stock price histories into a single DataFrame
    return pd.concat(stock_histories, axis=1)
    # Generate a dataset of 10 stock price histories with 250 days each
    multi_stock_history = generate_multiple_stock_histories(num_stocks=10, start_price=100, mean_return=0.05, volatility=0.2, num_days=250)

    # Plot the first 5 stock price histories
    multi_stock_history.iloc[:, :5].plot()
    plt.show()

stock = generate_multiple_stock_histories(10, 100, 0.5, 0.2, 10)
stock.plot()
plt.show()
