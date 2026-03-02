from fastapi import APIRouter


def wrap(data=None, error=None):
    return {"success": error is None, "data": data, "error": error}


def create_router(engine):
    router = APIRouter(prefix="/api/bot", tags=["bot"])

    @router.post("/start")
    async def start():
        await engine.start()
        return wrap({"running": True})

    @router.post("/stop")
    async def stop():
        await engine.stop()
        return wrap({"running": False})

    @router.post("/pause")
    async def pause():
        await engine.pause()
        return wrap({"paused": engine.state.paused})

    @router.get("/status")
    async def status():
        return wrap(engine.status())

    return router
