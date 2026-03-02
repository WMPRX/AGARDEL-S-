from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class BotState:
    running: bool = False
    paused: bool = False
    mode: str = "paper"
    started_at: datetime | None = None
    stats: dict[str, Any] = field(default_factory=lambda: {"trades": 0, "win_rate": 0.0, "pnl": 0.0})
    positions: list[dict[str, Any]] = field(default_factory=list)
    alerts: list[dict[str, Any]] = field(default_factory=list)
    signals: list[dict[str, Any]] = field(default_factory=list)
