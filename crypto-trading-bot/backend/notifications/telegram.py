import httpx


async def send_telegram(token: str, chat_id: str, message: str):
    if not token or not chat_id:
        return False
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(f"https://api.telegram.org/bot{token}/sendMessage", json={"chat_id": chat_id, "text": message})
        return r.status_code == 200
