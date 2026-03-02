import numpy as np


def correlation_guard(series_a, series_b, threshold: float = 0.8) -> bool:
    corr = np.corrcoef(series_a, series_b)[0, 1]
    return abs(corr) < threshold
