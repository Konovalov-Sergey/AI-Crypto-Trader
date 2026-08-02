import pandas as pd


class Indicators:

    @staticmethod
    def ema(df: pd.DataFrame, period: int = 20) -> pd.DataFrame:
        df[f"EMA{period}"] = (
            df["Close"]
            .ewm(span=period, adjust=False)
            .mean()
        )
        return df