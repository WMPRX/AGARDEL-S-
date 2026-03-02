import pandas as pd


def ema(series: pd.Series, period: int) -> pd.Series:
    return series.ewm(span=period, adjust=False).mean()


def adx(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high, low, close = df["high"], df["low"], df["close"]
    plus_dm = (high.diff()).clip(lower=0)
    minus_dm = (-low.diff()).clip(lower=0)
    tr = pd.concat([(high - low), (high - close.shift()).abs(), (low - close.shift()).abs()], axis=1).max(axis=1)
    atr = tr.rolling(period).mean()
    plus_di = 100 * (plus_dm.rolling(period).mean() / atr)
    minus_di = 100 * (minus_dm.rolling(period).mean() / atr)
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)).fillna(0) * 100
    return dx.rolling(period).mean().fillna(0)


def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    line = ema(series, fast) - ema(series, slow)
    signal_line = line.ewm(span=signal, adjust=False).mean()
    return line, signal_line
