from fastapi import APIRouter

def wrap(data=None, error=None):
    return {"success": error is None, "data": data, "error": error}


def create_router(engine):
    router = APIRouter(prefix="/api/trades", tags=["trades"])

    @router.get("")
    async def list_trades():
        return wrap([])

    @router.get("/open")
    async def open_trades():
        return wrap(engine.state.positions)

    @router.get("/stats")
    async def stats():
        return wrap(engine.state.stats)

    @router.post("/close/{trade_id}")
    async def close_trade(trade_id: int):
        return wrap({"closed": trade_id})

    return router
