class RiskManager:
    def __init__(self, max_daily_loss_pct=5.0, max_drawdown_pct=15.0, max_positions=3):
        self.max_daily_loss_pct = max_daily_loss_pct
        self.max_drawdown_pct = max_drawdown_pct
        self.max_positions = max_positions

    def can_trade(self, daily_pnl_pct: float, drawdown_pct: float, open_positions: int) -> tuple[bool, str]:
        if daily_pnl_pct < -self.max_daily_loss_pct:
            return False, "daily loss limit breached"
        if drawdown_pct > self.max_drawdown_pct:
            return False, "max drawdown exceeded"
        if open_positions >= self.max_positions:
            return False, "max concurrent positions reached"
        return True, "ok"
