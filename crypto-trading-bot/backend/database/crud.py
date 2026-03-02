from sqlalchemy import select
from database.models import Trade


async def list_trades(session, limit=100):
    q = await session.execute(select(Trade).order_by(Trade.timestamp.desc()).limit(limit))
    return q.scalars().all()
