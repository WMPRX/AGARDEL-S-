from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from config import settings
from exchanges.binance import BinanceExchange
from core.engine import BotEngine
from api.websocket import manager
from api.routers import bot, trades, strategies, backtest, portfolio, settings as settings_router

logger.remove()
logger.add(lambda msg: print(msg, end=""), serialize=True)

app = FastAPI(title="Crypto Trading Bot", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

exchange = BinanceExchange(settings.binance_api_key, settings.binance_api_secret, settings.binance_testnet)
engine = BotEngine(exchange)

app.include_router(bot.create_router(engine))
app.include_router(trades.create_router(engine))
app.include_router(strategies.create_router(engine))
app.include_router(backtest.create_router())
app.include_router(portfolio.create_router(engine))
app.include_router(settings_router.create_router())


@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/market/ticker/{symbol}")
async def ticker(symbol: str):
    return {"success": True, "data": {"symbol": symbol, "price": 65000, "change_24h": 1.2, "volume": 12345}, "error": None}


@app.get("/api/market/ohlcv/{symbol}")
async def ohlcv(symbol: str, timeframe: str = "1h", limit: int = 100):
    return {"success": True, "data": {"symbol": symbol, "timeframe": timeframe, "limit": limit, "candles": []}, "error": None}


@app.get("/api/market/orderbook/{symbol}")
async def orderbook(symbol: str):
    return {"success": True, "data": {"symbol": symbol, "bids": [], "asks": []}, "error": None}


@app.post("/api/demo/seed")
async def demo_seed():
    return {"success": True, "data": {"inserted": 100}, "error": None}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
            await manager.broadcast("bot_status", engine.status())
    except Exception:
        manager.disconnect(websocket)
