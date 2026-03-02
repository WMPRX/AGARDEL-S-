def atr_stop(entry: float, atr: float, multiplier: float, side: str) -> float:
    return entry - atr * multiplier if side == "BUY" else entry + atr * multiplier


def trailing_stop(current_stop: float, price: float, trail_pct: float, side: str) -> float:
    candidate = price * (1 - trail_pct) if side == "BUY" else price * (1 + trail_pct)
    return max(current_stop, candidate) if side == "BUY" else min(current_stop, candidate)
