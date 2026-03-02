import pandas as pd


def obv(df: pd.DataFrame):
    return (df["volume"] * (df["close"].diff().fillna(0).apply(lambda x: 1 if x > 0 else -1 if x < 0 else 0))).cumsum()


def vwap(df: pd.DataFrame):
    typical = (df["high"] + df["low"] + df["close"]) / 3
    return (typical * df["volume"]).cumsum() / df["volume"].cumsum()


def volume_profile(df: pd.DataFrame, bins: int = 20):
    return pd.cut(df["close"], bins=bins).value_counts().sort_index().to_dict()
