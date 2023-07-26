from enum import Enum
 
class Rank(Enum):
    ACE = ('A', 14)
    KING = ('K', 13)
    QUEEN = ('Q', 12)
    JACK = ('J', 11)
    TEN = ('10', 10)
    NINE = ('9', 9)
    EIGHT = ('8', 8)
    SEVEN = ('7', 7)
    SIX = ('6', 6)
    FIVE = ('5', 5)
    FOUR = ('4', 4)
    THREE = ('3', 3)
    TWO = ('2', 2)

    def __init__(self, rank:str, number:int):
        self._rank = rank
        self._number = number

    def __repr__(self):
        return self.value
    
    def __str__(self):
        return f'{self._rank}'