import httpx


async def send_discord(webhook: str, message: str, color: int = 5763719):
    if not webhook:
        return False
    payload = {"embeds": [{"description": message, "color": color}]}
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(webhook, json=payload)
        return r.status_code < 300
