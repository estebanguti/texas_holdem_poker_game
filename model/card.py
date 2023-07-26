from model.enums.rank import Rank
from model.enums.suit import Suit

class Card:

    def __init__(self, rank, suit):
        self._rank = Rank(rank)
        self._suit = Suit(suit)

    def __str__(self):
        return f'{self._rank} {self._suit.name}'
    
    def __repr__(self):
        return str(self)

