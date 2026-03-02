from abc import ABC, abstractmethod


class BaseExchange(ABC):
    @abstractmethod
    async def ticker(self, symbol: str) -> dict: ...

    @abstractmethod
    async def orderbook(self, symbol: str) -> dict: ...

    @abstractmethod
    async def ohlcv(self, symbol: str, timeframe: str = "1h", limit: int = 200): ...
