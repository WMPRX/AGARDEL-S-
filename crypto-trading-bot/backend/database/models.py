from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer, DateTime, Text
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Trade(Base):
    __tablename__ = "trades"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    symbol: Mapped[str] = mapped_column(String(32))
    side: Mapped[str] = mapped_column(String(8))
    entry_price: Mapped[float] = mapped_column(Float)
    exit_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    qty: Mapped[float] = mapped_column(Float)
    pnl: Mapped[float] = mapped_column(Float, default=0.0)
    fee: Mapped[float] = mapped_column(Float, default=0.0)
    strategy: Mapped[str] = mapped_column(String(64))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    status: Mapped[str] = mapped_column(String(16), default="open")


class BotConfig(Base):
    __tablename__ = "bot_config"
    key: Mapped[str] = mapped_column(String(64), primary_key=True)
    value: Mapped[str] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
