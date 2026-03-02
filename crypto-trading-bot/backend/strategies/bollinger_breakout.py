from .base_strategy import BaseStrategy
from indicators.volatility import bollinger_bands, atr


class BollingerBreakoutStrategy(BaseStrategy):
    name = "Bollinger Breakout"
    description = "Band breakout with ATR expansion"

    def generate_signals(self, df):
        upper, _, lower = bollinger_bands(df.close)
        a = atr(df)
        atr_expansion = a.iloc[-1] > a.tail(6).head(5).mean()
        c = df.close.iloc[-1]
        if c > upper.iloc[-1] and atr_expansion:
            return {"signal": "BUY", "confidence": 0.72, "reason": "upper breakout with ATR expansion"}
        if c < lower.iloc[-1] and atr_expansion:
            return {"signal": "SELL", "confidence": 0.72, "reason": "lower breakout with ATR expansion"}
        return {"signal": "HOLD", "confidence": 0.5, "reason": "breakout not validated"}
