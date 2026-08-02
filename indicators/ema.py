import pandas as pd


class EMA:

    @staticmethod
    def calculate(
        df: pd.DataFrame,
        period: int
    ) -> pd.DataFrame:

        df[f"EMA{period}"] = (
            df["Close"]
            .ewm(span=period, adjust=False)
            .mean()
        )

        return df