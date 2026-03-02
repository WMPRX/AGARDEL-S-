from fastapi import APIRouter
from config import settings

def wrap(data=None, error=None): return {"success": error is None, "data": data, "error": error}

def create_router():
    router = APIRouter(prefix="/api/settings", tags=["settings"])
    @router.get("")
    async def get_settings(): return wrap(settings.model_dump())
    @router.put("")
    async def update_settings(payload: dict): return wrap(payload)
    @router.post("/test-connection")
    async def test_connection(): return wrap({"latency_ms": 42, "account_balance": 10000})
    return router
