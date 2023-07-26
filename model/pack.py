from typing import List
from model.card import Card
from model.enums.rank import Rank
from model.enums.suit import Suit
import random

class Pack:
    
    def __init__(self):
        list:List[Card] = []
        for rank in Rank:
            for suit in Suit:
                list.append(Card(rank.value, suit.value))
        self.list = list

    def get_pack(self):
        list:List[Card] = self.list
        random.shuffle(list)
        return list
