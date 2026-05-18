import numpy as np
import pandas as pd
import yfinance as yf


def download_price_data(ticker, start_date, end_date):
    """
    Download historical price data from Yahoo Finance.
    """
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        raise ValueError("No data downloaded. Check ticker or date range.")

    return data


def calculate_returns(data):
    """
    Calculate daily percentage returns using adjusted close prices.
    """
    data = data.copy()

    if "Adj Close" in data.columns:
        price_col = "Adj Close"
    else:
        price_col = "Close"

    data["daily_return"] = data[price_col].pct_change()

    return data


def calculate_volatility(data):
    """
    Calculate daily and annualized volatility.
    """
    daily_volatility = data["daily_return"].std()
    annualized_volatility = daily_volatility * np.sqrt(252)

    return daily_volatility, annualized_volatility


def main():
    ticker = "AAPL"
    start_date = "2023-01-01"
    end_date = "2024-01-01"

    data = download_price_data(ticker, start_date, end_date)
    data = calculate_returns(data)

    daily_vol, annualized_vol = calculate_volatility(data)

    print(f"Ticker: {ticker}")
    print(f"Daily Volatility: {daily_vol:.4f}")
    print(f"Annualized Volatility: {annualized_vol:.4f}")
    print(f"Annualized Volatility %: {annualized_vol * 100:.2f}%")


if __name__ == "__main__":
    main()
