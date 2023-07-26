from collections import Counter
from itertools import groupby
from operator import itemgetter
from typing import List
from model.card import Card
from model.enums.play_type import PlayType
from model.enums.rank import Rank
from model.play_hand import PlayHand

class PlayHandService:

    def get_player_hand(cls, cards: List[Card]):
        play_hand = PlayType.HIGH_CARD
        cards_hand = cls.order_by_highest_cards(cards)
        if (cls.has_one_pair(cards)):
            play_hand = PlayType.ONE_PAIR
            cards_hand = cls.get_one_pair_hand(cards)
        if (cls.has_two_pair(cards)):
            play_hand = PlayType.TWO_PAIR
            cards_hand = cls.get_two_pair_hand(cards)
        if (cls.has_three_of_a_kind(cards)):
            play_hand = PlayType.THREE_OF_A_KIND
            cards_hand = cls.get_three_of_a_kind_hand(cards)
        if (cls.has_straight(cards)):
            play_hand = PlayType.STRAIGHT
            cards_hand = cls.get_straight_hand(cards)
        if (cls.has_flush(cards)):
            play_hand = PlayType.FLUSH
            cards_hand = cls.get_flush_hand(cards)
        if (cls.has_full_house(cards)):
            play_hand = PlayType.FULL_HOUSE
            cards_hand = cls.get_full_house_hand(cards)
        if (cls.has_poker(cards)):
            play_hand = PlayType.POKER
            cards_hand = cls.get_poker_hand(cards)
        if (cls.has_straight_flush(cards)):
            play_hand = PlayType.STRAIGHT_FLUSH
            cards_hand = cls.get_straight_flush_hand(cards)
        if (cls.has_royal_flush(cards)):
            play_hand = PlayType.ROYAL_FLUSH
            cards_hand = cls.get_royal_flush_hand(cards)
        return PlayHand(play_hand, cards_hand)
    
    def has_one_pair(cls, cards):
        list = [obj._rank for obj in cards]
        return len([k for k,v in Counter(list).items() if v==2]) >= 1
    
    def has_two_pair(cls, cards):
        list = [obj._rank for obj in cards]
        return len([k for k,v in Counter(list).items() if v==2]) >= 2
    
    def has_three_of_a_kind(cls, cards):
        list = [obj._rank for obj in cards]
        return len([k for k,v in Counter(list).items() if v==3]) >= 1
    
    def has_straight(cls, cards):
        data = [card._rank._number for card in cards]
        if (data.__contains__(14)):
            data.append(1)
        data.sort()
        consecutive = []
        for k, g in groupby(enumerate(data), lambda ix : ix[0] - ix[1]):
            consecutive.append(list(map(itemgetter(1), g)))
        try:
            straight_cards = next(filter(lambda c: len(c) >= 5, consecutive))
        except StopIteration as e:
            straight_cards = []
        return straight_cards != []
    
    def has_flush(cls, cards):
        list = [obj._suit for obj in cards]
        return len([k for k,v in Counter(list).items() if v==5]) == 1
    
    def has_full_house(cls, cards):
        list = [obj._rank for obj in cards]
        return ((len([k for k,v in Counter(list).items() if v==3]) == 1 and len([k for k,v in Counter(list).items() if v==2]) >= 1) or 
                (len([k for k,v in Counter(list).items() if v==3]) == 2))
    
    def has_poker(cls, cards):
        list = [obj._rank for obj in cards]
        return len([k for k,v in Counter(list).items() if v==4]) == 1
    
    def has_straight_flush(cls, cards):
        return cls.has_straight(cards) and cls.has_flush(cards)

    def has_royal_flush(cls, cards):
        list = [obj._rank for obj in cards]
        ranks = sorted([14 if rank._number == 2 else rank._number for rank in list])
        return (cls.has_straight_flush(cards) and ranks[0] == 10 and ranks[-1] == 14) 
    
    def order_by_highest_cards(cls, cards):
        cards.sort(key = lambda c: c._rank._number, reverse=True)
        return cards[:5] if len(cards) > 5 else cards

    def get_one_pair_hand(cls, cards):
        one_pair_cards = []
        othercards = []
        for i in cards:
            card = i
            count = 0
            for j in cards:
                if card._rank._rank == j._rank._rank:
                    count += 1
            if count == 2:
                one_pair_cards.append(card)
            else:
                othercards.append(card)
        cards_high = cls.order_by_highest_cards(othercards)[:3]
        one_pair_cards.extend(cards_high)
        return one_pair_cards 

    def get_two_pair_hand(cls, cards):
        two_pair_cards = []
        othercards = []
        for i in cards:
            card = i
            count = 0
            for j in cards:
                if card._rank._rank == j._rank._rank:
                    count += 1
            if count == 2:
                two_pair_cards.append(card)
            else:
                othercards.append(card)
        if len(two_pair_cards) > 4:
            two_pair_cards = sorted(two_pair_cards, key=lambda c: c._rank._number, reverse=True)
            othercards.extend(two_pair_cards[-2:])
            two_pair_cards = two_pair_cards[:4]
        cards_high = cls.order_by_highest_cards(othercards)[:1]
        two_pair_cards.extend(cards_high)
        return two_pair_cards

    def get_three_of_a_kind_hand(cls, cards):
        three_of_a_kind_cards = []
        othercards = []
        for i in cards:
            card = i
            count = 0
            for j in cards:
                if card._rank._rank == j._rank._rank:
                    count += 1
            if count == 3:
                three_of_a_kind_cards.append(card)
            else:
                othercards.append(card)
        cards_high = cls.order_by_highest_cards(othercards)[:2]
        three_of_a_kind_cards.extend(cards_high)
        return three_of_a_kind_cards
    
    def get_straight_hand(cls, cards):
        data = list(set([card._rank._number for card in cards]))
        if (data.__contains__(14)):
            data.append(1)
        data.sort()
        consecutive = []
        straight_numbers = []
        straight_cards = []
        for k, g in groupby(enumerate(data), lambda ix : ix[0] - ix[1]):
            consecutive.append(list(map(itemgetter(1), g)))
        try:
            straight_numbers = next(filter(lambda c: len(c) >= 5, consecutive))
        except StopIteration as e:
            straight_numbers = []
        for i in straight_numbers:
            if i == 1:
                card = next(filter(lambda c: c._rank._number == 14, cards))
                
            else:
                card = next(filter(lambda c: c._rank._number == i, cards))
            straight_cards.append(card)
        straight_cards = cls.order_by_highest_cards(straight_cards)
        if (len(straight_cards) == 5 and sum([card._rank._number for card in straight_cards]) == 28):
            straight_cards.append(straight_cards.pop(0))
        return straight_cards[:5]
    
    def get_flush_hand(cls, cards):
        flush_cards = []
        for i in cards:
            card = i
            count = 0
            for j in cards:
                if card._suit == j._suit:
                    count += 1
            if count >= 5:
                flush_cards.append(card)
        flush_cards = cls.order_by_highest_cards(flush_cards)[:5]
        return flush_cards

    def get_full_house_hand(cls, cards):
        full_house_cards = []
        two_pair_cards = []
        for i in cards:
            card = i
            count = 0
            for j in cards:
                if card._rank._rank == j._rank._rank:
                    count += 1
            if count == 3:
                full_house_cards.append(card)
            if count == 2:
                two_pair_cards.append(card)
        if len(full_house_cards) > 3:
            third_of_a_kind_cards = cls.order_by_highest_cards(full_house_cards)
            full_house_cards = third_of_a_kind_cards[:3]
            two_pair_cards.extend(third_of_a_kind_cards[3:])
        if len(two_pair_cards) > 2:
            two_pair_cards = cls.order_by_highest_cards(two_pair_cards)[:2]
        full_house_cards.extend(two_pair_cards)
        return full_house_cards
    
    def get_poker_hand(cls, cards):
        poker_cards = []
        othercards = []
        for i in cards:
            card = i
            count = 0
            for j in cards:
                if card._rank._rank == j._rank._rank:
                    count += 1
            if count == 4:
                poker_cards.append(card)
            else:
                othercards.append(card)
        cards_high = cls.order_by_highest_cards(othercards)[:1]
        poker_cards.extend(cards_high)
        return poker_cards
    
    def get_straight_flush_hand(cls, cards):
        straight_flush_cards = []
        flush_cards = []
        for i in cards:
            card = i
            count = 0
            for j in cards:
                if card._suit == j._suit:
                    count += 1
            if count >= 5:
                flush_cards.append(card)
        ranks = list(set([card._rank._number for card in flush_cards]))
        for i in range(len(ranks)):
            card = next(filter(lambda c: c._rank._number == ranks[i], cards))
            if ranks[i] + 1 in ranks or ranks[i] - 1 in ranks:
                straight_flush_cards.append(card)
            if ranks[i] == 14 and ranks[i] - 12 in ranks and ranks[i] - 9 in ranks:
                straight_flush_cards.append(card)
        straight_flush_cards = cls.order_by_highest_cards(straight_flush_cards)
        if (len(straight_flush_cards) == 5 and sum([card._rank._number for card in straight_flush_cards]) == 28):
            straight_flush_cards.append(straight_flush_cards.pop(0))
        return straight_flush_cards[:5]
    
    def get_royal_flush_hand(cls, cards):
        royal_flush_cards = cls.get_straight_flush_hand(cards)
        return royal_flush_cards if royal_flush_cards[0]._rank == Rank.ACE and royal_flush_cards[-1]._rank == Rank.TEN else []