import pandas as pd
from indicators.trend import ema, adx
from .base_strategy import BaseStrategy


class EmaCrossoverStrategy(BaseStrategy):
    name = "EMA Crossover"
    description = "EMA 9/21 with ADX confirmation"

    def generate_signals(self, df: pd.DataFrame) -> dict:
        fast = self.parameters.get("fast_period", 9)
        slow = self.parameters.get("slow_period", 21)
        adx_threshold = self.parameters.get("adx_threshold", 25)
        df = df.copy()
        df["ema_fast"], df["ema_slow"], df["adx"] = ema(df.close, fast), ema(df.close, slow), adx(df)
        last, prev = df.iloc[-1], df.iloc[-2]
        if prev.ema_fast <= prev.ema_slow and last.ema_fast > last.ema_slow and last.adx > adx_threshold:
            return {"signal": "BUY", "confidence": 0.82, "reason": "bullish crossover + trend strength"}
        if prev.ema_fast >= prev.ema_slow and last.ema_fast < last.ema_slow and last.adx > adx_threshold:
            return {"signal": "SELL", "confidence": 0.82, "reason": "bearish crossover + trend strength"}
        return {"signal": "HOLD", "confidence": 0.5, "reason": "no valid crossover"}
