import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


ticker = "SPY"
start_date = "2020-01-01"
end_date = "2024-01-01"

data = yf.download(ticker, start=start_date, end=end_date)

data["return"] = data["Adj Close"].pct_change()

data["rolling_volatility"] = (
    data["return"]
    .rolling(window=30)
    .std() * np.sqrt(252)
)

print(data[["rolling_volatility"]].tail())

data["rolling_volatility"].plot(
    figsize=(12, 6),
    title=f"{ticker} Rolling 30-Day Annualized Volatility"
)

plt.xlabel("Date")
plt.ylabel("Volatility")
plt.savefig("outputs/rolling_volatility.png")
plt.show()
