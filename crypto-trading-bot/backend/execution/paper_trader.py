def simulate_fill(price: float, slippage_pct: float = 0.05):
    return price * (1 + slippage_pct / 100)
