from fastapi import APIRouter

def wrap(data=None, error=None): return {"success": error is None, "data": data, "error": error}

def create_router(engine):
    router = APIRouter(prefix="/api/strategies", tags=["strategies"])
    @router.get("")
    async def list_strategies():
        s = engine.strategy
        return wrap([{"id": 1, "name": s.name, "description": s.description, "parameters": s.parameters, "enabled": s.enabled, "timeframe": s.timeframe}])
    @router.put("/{strategy_id}")
    async def update(strategy_id: int, payload: dict):
        engine.strategy.parameters.update(payload)
        return wrap({"id": strategy_id, "parameters": engine.strategy.parameters})
    @router.post("/{strategy_id}/enable")
    async def enable(strategy_id: int):
        engine.strategy.enabled = True; return wrap({"id": strategy_id, "enabled": True})
    @router.post("/{strategy_id}/disable")
    async def disable(strategy_id: int):
        engine.strategy.enabled = False; return wrap({"id": strategy_id, "enabled": False})
    return router
