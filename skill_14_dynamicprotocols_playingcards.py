from dataclasses import dataclass
from icecream import ic
from itertools import product
import random

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
            self._cards = [PlayingCard(*args) for args in product(self.SUITS, self.RANKS)]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, item):
        if type(item) == slice:
            return CardDeck(self._cards[item])
        
        return self._cards[item]
    
    def __add__(self, other):
        if type(other) == PlayingCard:
            return CardDeck([*self._cards, other])
        elif type(other) == CardDeck:
            return CardDeck([*self._cards, *other._cards])
        
    def __radd__(self, other):
        return self + other
    
    def __mul__(self, other):
        if type(other) == int:
            return CardDeck(self._cards * other)
        
    def __rmul__(self, other):
        return self * other
    
    def draw(self, n=1):
        drawn_cards = list()

        for i in range(n):
            idx = random.randrange(len(self))
            drawn_cards.append(self._cards.pop(idx))
        #randomly pick an index to draw from. 
        #take that item out

        if n == 1: 
            return drawn_cards[0]
        else:
            return CardDeck(drawn_cards)
        
    def __repr__(self) -> str:
        return f"CardDeck(cards={repr(self._cards)})"
        
if __name__ == "__main__":
    shuffle_1 = CardDeck()

    ic(shuffle_1)

    shuffle_2 = CardDeck(cards=[PlayingCard('spades', '4')])
    ic("*******************************")
    ic(shuffle_2)

    ic(shuffle_2 + PlayingCard('spades', '5'))

    ic(PlayingCard('spades', '5') in shuffle_2 + PlayingCard('spades', '5'))

    shuffle_3 = CardDeck(cards=[PlayingCard('spades', '4'), PlayingCard('hearts', 'King')])
    ic("*******************************")
    ic(shuffle_3)

    for card in shuffle_3:
        ic(card.rank)

    # shuffle_4 = CardDeck(PlayingCard('spades', '4', '4'), PlayingCard('hearts', 'King'))

    # ic(shuffle_4)



            



    

