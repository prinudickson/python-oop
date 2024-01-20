from icecream import ic
from dataclasses import dataclass
from functools import total_ordering
from typing import List

@dataclass(frozen=True)
class Stock:
    """
    Contains the stock attributes of ticker, price, divident, divident frequency
    """
    ticker: str
    price: float
    divident: float
    divident_freq: int

    @property
    def annual_divident(self):
        x = self.divident * self.divident_freq
        #print(x)
        return x
    
@dataclass
@total_ordering
class Position:
    """
    Contains Stock and the total number of shares.
    """
    stock: Stock
    shares: float

    def __lt__(self, other):
        if type(other) != Position:
            raise TypeError("Can only compare instance of Position")

        return self.stock.price * self.shares < other.stock.price * other.shares

    def __eq__(self, other):
        if type(other) != Position:
            raise TypeError("Can only compare instance of Position")

        return self.stock.price * self.shares == other.stock.price * other.shares


@dataclass
class Portfolio:
    """
    Contains all the various positions
    """
    holdings: List[Position]

    @property
    def value(self):
        total_value = sum([position.stock.price * position.shares for position in self.holdings])
        return total_value

    @property
    def portfolio_yield(self):
        total_dividends = sum([position.stock.annual_dividend * position.shares for position in self.holdings])

        return round((total_dividends / self.value), 6)



if __name__ == "__main__":
    s1 = Stock("GGL", 3.14, 0.03, 4)
    ic(s1)
    ic(s1.annual_divident)

    s2 = Stock("MSFT", 20.04, 0.07, 4)
    ic(s2)
    ic(s2.annual_divident)

    p1 = Position(s1, 200)
    ic(p1)

    p2 = Position(s2, 100)
    ic(p2)

    pf = Portfolio([p1, p2])
    ic(pf)