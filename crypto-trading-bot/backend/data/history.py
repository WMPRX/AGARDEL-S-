from sqlalchemy import text


async def ensure_history_table(session):
    await session.execute(text("CREATE TABLE IF NOT EXISTS ohlcv_cache (symbol TEXT, timeframe TEXT, timestamp INTEGER, open REAL, high REAL, low REAL, close REAL, volume REAL)"))
