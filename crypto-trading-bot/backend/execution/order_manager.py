class OrderManager:
    def place_order(self, symbol: str, side: str, qty: float, price: float):
        return {"symbol": symbol, "side": side, "qty": qty, "price": price, "status": "placed"}
