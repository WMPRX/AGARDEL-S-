import numpy as np


def sharpe(returns):
    r = np.array(returns)
    return float((r.mean() / (r.std() + 1e-9)) * np.sqrt(252))
