def top_of_book(orderbook: dict) -> dict:
    bid = orderbook.get("bids", [[0, 0]])[0]
    ask = orderbook.get("asks", [[0, 0]])[0]
    return {"best_bid": bid[0], "best_ask": ask[0], "spread": ask[0] - bid[0]}
