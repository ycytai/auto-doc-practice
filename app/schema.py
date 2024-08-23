from typing import TypedDict


class StockPrice(TypedDict):
    date: str
    symbol: str
    open: str
    high: str
    low: str
    close: str
    volume: str
    values: str

class StockPriceResponse(TypedDict):
    status: str
    msg: str
    data: list[StockPrice]
