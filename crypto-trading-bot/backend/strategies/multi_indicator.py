from .base_strategy import BaseStrategy
from indicators.trend import ema, macd, adx
from indicators.momentum import rsi


class MultiIndicatorStrategy(BaseStrategy):
    name = "Multi Indicator"
    description = "Score from trend, momentum, volume, strength"

    def generate_signals(self, df):
        score = 0
        if ema(df.close, 9).iloc[-1] > ema(df.close, 21).iloc[-1]: score += 20
        if 40 < rsi(df.close).iloc[-1] < 70: score += 20
        m, s = macd(df.close)
        if m.iloc[-1] > s.iloc[-1]: score += 20
        if df.volume.iloc[-1] > df.volume.rolling(20).mean().iloc[-1]: score += 20
        if adx(df).iloc[-1] > 25: score += 20
        if score > 60: return {"signal": "BUY", "confidence": score / 100, "reason": f"score {score}"}
        if score < 40: return {"signal": "SELL", "confidence": (100-score)/100, "reason": f"score {score}"}
        return {"signal": "HOLD", "confidence": 0.5, "reason": f"neutral score {score}"}
