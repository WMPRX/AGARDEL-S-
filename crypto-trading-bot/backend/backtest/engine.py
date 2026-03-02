import pandas as pd
from backtest.metrics import sharpe


def run_backtest(df: pd.DataFrame, signal_col: str = "signal", initial_capital: float = 10000):
    cash, position = initial_capital, 0.0
    equity = []
    for _, row in df.iterrows():
        if row[signal_col] == 1 and cash > 0:
            position = cash / row.close
            cash = 0
        elif row[signal_col] == -1 and position > 0:
            cash = position * row.close
            position = 0
        equity.append(cash + position * row.close)
    returns = pd.Series(equity).pct_change().fillna(0)
    return {"total_return_pct": (equity[-1] / initial_capital - 1) * 100 if equity else 0, "sharpe": sharpe(returns)}
