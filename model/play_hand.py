from typing import List
from model.card import Card
from model.enums.play_type import PlayType

class PlayHand:

    def __init__(self, play_type: PlayType, cards: List[Card]):
        self._play_type = play_type
        self._cards = cards

    def __str__(self):
        return f'{self._play_type.name} {self._cards}'

    def __repr__(self):
        return str(self)