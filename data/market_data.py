import yfinance as yf
import pandas as pd


class MarketData:

    def __init__(self):
        print("MarketData initialized")

    def load_history(
        self,
        symbol="BTC-USD",
        period="6mo",
        interval="1h"
    ) -> pd.DataFrame:

        df = yf.download(
            symbol,
            period=period,
            interval=interval,
            auto_adjust=True,
            progress=False
        )

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        return df