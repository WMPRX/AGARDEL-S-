from .base_strategy import BaseStrategy
from indicators.trend import macd


class MacdMomentumStrategy(BaseStrategy):
    name = "MACD Momentum"
    description = "MACD cross with volume confirmation"

    def generate_signals(self, df):
        line, sig = macd(df.close)
        vol_ok = df.volume.iloc[-1] > (df.volume.rolling(20).mean().iloc[-1] * 1.5)
        if line.iloc[-2] <= sig.iloc[-2] and line.iloc[-1] > sig.iloc[-1] and vol_ok:
            return {"signal": "BUY", "confidence": 0.74, "reason": "MACD bullish cross + high volume"}
        if line.iloc[-2] >= sig.iloc[-2] and line.iloc[-1] < sig.iloc[-1] and vol_ok:
            return {"signal": "SELL", "confidence": 0.74, "reason": "MACD bearish cross + high volume"}
        return {"signal": "HOLD", "confidence": 0.5, "reason": "momentum filter unmet"}
