from typing import List
from model.card import Card
from model.pack import Pack

class Croupier:

    _cards: List[Card] = []

    def __init__(self, pack: Pack):
        self._pack = pack.get_pack()

    def deal_card(self):
        return self._pack.pop(0)

    def flop(self):
        print('Show flop')
        i = 0
        while (i<3):
            card = self._pack.pop(i)
            self._cards.append(card)
            i=i+1
        print(self._cards)
        return self._cards
    
    def turn(self):
        print('Show turn')
        card = self._pack.pop(0)
        print(card)
        self._cards.append(card)
        return card

    def river(self):
        print('Show river')
        card = self._pack.pop(0)
        print(card)
        self._cards.append(card)
        return card

