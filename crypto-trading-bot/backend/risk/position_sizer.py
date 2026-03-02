def fixed_percentage_size(portfolio_value: float, risk_pct: float, price: float) -> float:
    return max((portfolio_value * (risk_pct / 100.0)) / max(price, 1e-9), 0.0)


def kelly_size(portfolio_value: float, reward_risk: float, win_rate: float, price: float) -> float:
    q = 1 - win_rate
    frac = max(min(((reward_risk * win_rate) - q) / max(reward_risk, 1e-9), 0.1), 0.0)
    return (portfolio_value * frac) / max(price, 1e-9)
