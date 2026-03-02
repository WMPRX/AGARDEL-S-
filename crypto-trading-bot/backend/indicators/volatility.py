import pandas as pd


def atr(df: pd.DataFrame, period: int = 14):
    tr = pd.concat([(df["high"] - df["low"]), (df["high"] - df["close"].shift()).abs(), (df["low"] - df["close"].shift()).abs()], axis=1).max(axis=1)
    return tr.rolling(period).mean()


def bollinger_bands(series: pd.Series, period: int = 20, std_dev: float = 2.0):
    mid = series.rolling(period).mean()
    std = series.rolling(period).std()
    return mid + std * std_dev, mid, mid - std * std_dev
