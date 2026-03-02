from abc import ABC, abstractmethod
import pandas as pd


class BaseStrategy(ABC):
    name: str
    description: str

    def __init__(self, parameters: dict, timeframe: str = "1h", enabled: bool = True):
        self.parameters = parameters
        self.timeframe = timeframe
        self.enabled = enabled

    @abstractmethod
    def generate_signals(self, df: pd.DataFrame) -> dict:
        raise NotImplementedError
