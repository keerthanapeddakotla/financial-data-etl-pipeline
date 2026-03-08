import yfinance as yf
import pandas as pd

def extract_data():

    tickers = ["AAPL", "MSFT", "TSLA", "NVDA"]

    try:
        data = yf.download(
            tickers,
            start="2023-01-01",
            end="2024-01-01",
            group_by="ticker",
            progress=False
        )

        close_prices = pd.DataFrame()

        for ticker in tickers:
            if ticker in data:
                close_prices[ticker] = data[ticker]["Close"]

        close_prices.reset_index(inplace=True)

        return close_prices

    except Exception as e:
        print("Error downloading data:", e)
        return pd.DataFrame()