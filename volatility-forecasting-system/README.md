# Volatility Forecasting System

This project analyzes and forecasts market volatility using real-world financial market data.

The project focuses on understanding how volatility behaves over time and how quantitative researchers estimate and forecast market risk using statistical and machine learning techniques.

## Objectives

- Download historical financial market data
- Calculate daily asset returns
- Estimate historical volatility
- Compute annualized volatility
- Analyze rolling realized volatility
- Visualize volatility regimes and market stress periods
- Compare volatility forecasting models

## Initial Asset

The first asset analyzed in this project is:

- SPY (SPDR S&P 500 ETF)

SPY is widely used as a benchmark for the U.S. equity market and is commonly used in quantitative finance research.

## Methodology

### Step 1 — Historical Market Data

Historical market prices are downloaded using the `yfinance` API.

### Step 2 — Daily Return Calculation

Daily returns are calculated using percentage price changes:

```python
daily_return = Close.pct_change()
