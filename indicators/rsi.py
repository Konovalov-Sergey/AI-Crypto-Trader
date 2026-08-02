import pandas as pd


class RSI:

    @staticmethod
    def calculate(
        df: pd.DataFrame,
        period: int = 14
    ) -> pd.DataFrame:

        delta = df["Close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(period).mean()
        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        df["RSI"] = 100 - (100 / (1 + rs))

        return df