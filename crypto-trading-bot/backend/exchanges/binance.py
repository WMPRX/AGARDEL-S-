import ccxt.async_support as ccxt
from .base import BaseExchange


class BinanceExchange(BaseExchange):
    def __init__(self, api_key="", secret="", testnet=True):
        self.client = ccxt.binance({"apiKey": api_key, "secret": secret, "enableRateLimit": True})
        if testnet:
            self.client.set_sandbox_mode(True)

    async def ticker(self, symbol):
        return await self.client.fetch_ticker(symbol)

    async def orderbook(self, symbol):
        return await self.client.fetch_order_book(symbol)

    async def ohlcv(self, symbol, timeframe="1h", limit=200):
        return await self.client.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
