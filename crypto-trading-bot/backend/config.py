from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    exchange: str = "binance"
    trading_mode: str = "paper"
    binance_api_key: str = ""
    binance_api_secret: str = ""
    binance_testnet: bool = True
    okx_api_key: str = ""
    okx_api_secret: str = ""
    okx_passphrase: str = ""
    bybit_api_key: str = ""
    bybit_api_secret: str = ""

    default_symbol: str = "BTC/USDT"
    default_timeframe: str = "1h"
    max_concurrent_positions: int = 3
    position_size_method: str = "fixed"
    position_size_pct: float = 1.0
    max_daily_loss_pct: float = 5.0
    max_drawdown_pct: float = 15.0
    atr_multiplier: float = 2.0
    trailing_stop: bool = False

    database_url: str = "sqlite:///./trading_bot.db"

    telegram_bot_token: str = ""
    telegram_chat_id: str = ""
    discord_webhook_url: str = ""

    secret_key: str = "change-me-in-production"
    backend_port: int = 8000
    frontend_port: int = 3000
    log_level: str = "INFO"


settings = Settings()
