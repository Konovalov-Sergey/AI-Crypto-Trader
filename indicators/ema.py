import pandas as pd


def ema(data: pd.Series, period: int) -> pd.Series:
    """
    Exponential Moving Average (EMA)
    """
    return data.ewm(span=period, adjust=False).mean()