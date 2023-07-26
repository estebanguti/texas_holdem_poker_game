from enum import Enum

class PlayType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    POKER = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10