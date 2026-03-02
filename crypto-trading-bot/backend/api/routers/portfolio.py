from fastapi import APIRouter

def wrap(data=None, error=None): return {"success": error is None, "data": data, "error": error}

def create_router(engine):
    router = APIRouter(prefix="/api/portfolio", tags=["portfolio"])
    @router.get("")
    async def current(): return wrap({"holdings": engine.state.positions, "balance": 10000, "total_value": 10000})
    @router.get("/history")
    async def history(): return wrap([])
    @router.get("/snapshot")
    async def snapshot(): return wrap({"total_value": 10000, "available_balance": 10000, "positions": engine.state.positions})
    return router
