def best_price(orderbooks: list[dict], side: str = "BUY"):
    if side == "BUY":
        return min(ob["asks"][0][0] for ob in orderbooks if ob.get("asks"))
    return max(ob["bids"][0][0] for ob in orderbooks if ob.get("bids"))
