from .base_strategy import BaseStrategy
from indicators.momentum import rsi
from indicators.volatility import bollinger_bands


class RsiMeanReversionStrategy(BaseStrategy):
    name = "RSI Mean Reversion"
    description = "RSI extremes with Bollinger confirmation"

    def generate_signals(self, df):
        r = rsi(df.close).iloc[-1]
        up, _, low = bollinger_bands(df.close)
        c = df.close.iloc[-1]
        if r < 30 and c <= low.iloc[-1]:
            return {"signal": "BUY", "confidence": 0.76, "reason": "oversold at lower band"}
        if r > 70 and c >= up.iloc[-1]:
            return {"signal": "SELL", "confidence": 0.76, "reason": "overbought at upper band"}
        return {"signal": "HOLD", "confidence": 0.5, "reason": "mean reversion not triggered"}
