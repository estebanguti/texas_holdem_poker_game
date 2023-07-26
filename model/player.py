from typing import List
from model.card import Card
from model.play_hand import PlayHand

class Player:

    _play_hand: PlayHand = None
    _cards: list[Card] = []

    def __init__(self, name: str):
        self._name = name

    def show_hand(self):
        print(self._play_hand)

    def fold(self):
        print('Fold')

    def bet(self):
        print('Bet')

    def call(self):
        print('Call')

    def raise_bet(self):
        print('Raise')