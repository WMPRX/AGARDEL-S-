from fastapi import APIRouter

def wrap(data=None, error=None): return {"success": error is None, "data": data, "error": error}

def create_router():
    router = APIRouter(prefix="/api/backtest", tags=["backtest"])
    jobs = {}
    @router.post("/run")
    async def run(payload: dict):
        job_id = str(len(jobs)+1); jobs[job_id] = {"progress": 100, "result": {"message": "backtest completed", "input": payload}}
        return wrap({"job_id": job_id})
    @router.get("/status/{job_id}")
    async def status(job_id: str): return wrap({"progress": jobs.get(job_id, {}).get("progress", 0)})
    @router.get("/results/{job_id}")
    async def results(job_id: str): return wrap(jobs.get(job_id, {}).get("result", {}))
    @router.get("/history")
    async def history(): return wrap(list(jobs.keys()))
    return router
