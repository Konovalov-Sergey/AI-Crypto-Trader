import pandas as pd


class EmaRsiStrategy:

    @staticmethod
    def generate_signals(df: pd.DataFrame) -> pd.DataFrame:

        df["Signal"] = "HOLD"

        # Перетин EMA знизу вгору
        buy = (
            (df["EMA20"] > df["EMA50"]) &
            (df["EMA20"].shift(1) <= df["EMA50"].shift(1)) &
            (df["RSI"] > 50)
        )

        # Перетин EMA зверху вниз
        sell = (
            (df["EMA20"] < df["EMA50"]) &
            (df["EMA20"].shift(1) >= df["EMA50"].shift(1)) &
            (df["RSI"] < 50)
        )

        df.loc[buy, "Signal"] = "BUY"
        df.loc[sell, "Signal"] = "SELL"

        return df