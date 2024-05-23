from dataclasses import dataclass
from icecream import ic
from itertools import product

@dataclass()
class PlayingCard:
    suit: str
    rank: str

    def __post_init__(self):
        self.suit = self.suit.lower()
        self.rank = self.rank.lower()

@dataclass()
class CardDeck:
    SUITS = ['spades', 'diamonds', 'clubs', 'hearts']
    RANKS = list('ajkq') + list(str(n) for n in range(2,11))

    @staticmethod
    def _filter_playing_cards(from_sequence):
        return list(filter(lambda a: type(a)==PlayingCard, from_sequence))

    def __init__(self, cards=None) -> None:
        playing_cards = None
        if type(cards) == list and len(cards) > 0:
            #find the valid cards in the list, if any
            playing_cards = self._filter_playing_cards(cards)

        if playing_cards:
            self._cards = playing_cards
        else:
            #full deck
            self._cards = product(self.SUITS, self.RANKS)

    def __len__(self):
        return len(self._cards)
            



    

