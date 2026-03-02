import asyncio
from datetime import datetime
from core.state import BotState
from strategies.ema_crossover import EmaCrossoverStrategy


class BotEngine:
    def __init__(self, exchange):
        self.exchange = exchange
        self.state = BotState()
        self.task = None
        self.strategy = EmaCrossoverStrategy({"fast_period": 9, "slow_period": 21, "adx_threshold": 25})

    async def start(self):
        if self.state.running:
            return
        self.state.running = True
        self.state.started_at = datetime.utcnow()
        self.task = asyncio.create_task(self._loop())

    async def stop(self):
        self.state.running = False
        if self.task:
            self.task.cancel()

    async def pause(self):
        self.state.paused = not self.state.paused

    def status(self):
        uptime = int((datetime.utcnow() - self.state.started_at).total_seconds()) if self.state.started_at else 0
        return {"running": self.state.running, "mode": self.state.mode, "uptime": uptime, "stats": self.state.stats}

    async def _loop(self):
        while self.state.running:
            await asyncio.sleep(2)
