import pandas as pd


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta.clip(upper=0)).rolling(period).mean()
    rs = gain / loss.replace(0, 1e-9)
    return 100 - (100 / (1 + rs))


def stochastic(df: pd.DataFrame, period: int = 14):
    low_min = df["low"].rolling(period).min()
    high_max = df["high"].rolling(period).max()
    return ((df["close"] - low_min) / (high_max - low_min + 1e-9)) * 100


def cci(df: pd.DataFrame, period: int = 20):
    tp = (df["high"] + df["low"] + df["close"]) / 3
    sma = tp.rolling(period).mean()
    mad = (tp - sma).abs().rolling(period).mean()
    return (tp - sma) / (0.015 * mad + 1e-9)
