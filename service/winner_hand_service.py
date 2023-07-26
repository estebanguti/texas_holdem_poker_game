from typing import List
from model.enums.play_type import PlayType
from model.play_hand import PlayHand
from model.player import Player

class WinnerHandService:

    def get_winner_players(cls, players: List[Player]):
        winner_players = []
        hands: List[PlayHand] = [player._play_hand for player in players]
        winner_hands = cls.get_winner_hand(hands)
        for player in players:
            if winner_hands.__contains__(player._play_hand):
                winner_players.append(player)
        return winner_players

    def get_winner_hand(cls, player_hands: List[PlayHand]):
        hands: List[PlayHand] = cls.get_the_highest_hands_by_play_type(player_hands)
        if len(hands) > 1:
            hands = cls.get_highest_hand(hands)
        return hands

    def get_the_highest_hands_by_play_type(cls, player_hands: List[PlayHand]):
        highest_hands = []
        play_types = [hand._play_type.value for hand in player_hands]
        max_value = PlayType(max(play_types))
        for hand in player_hands:
            if hand._play_type == max_value:
                highest_hands.append(hand)
        return highest_hands
    
    def get_highest_hand_by_total_amount_hand(cls, hands: List[PlayHand]):
        highest_hand = []
        max_sum = max(sum(card._rank._number for card in hand._cards) for hand in hands)
        for hand in hands:
            sum_hand = sum(card._rank._number for card in hand._cards)
            if sum_hand == max_sum:
                highest_hand.append(hand)
        return highest_hand
    
    def get_highest_hand(cls, hands: List[PlayHand]):
        highest_hands = []
        play_type = list(set(card._play_type for card in hands))[0]
        if play_type == PlayType.HIGH_CARD:
            numbers = list()
            for hand in hands:
                for card in hand._cards:
                    numbers.append(card._rank._number) 
            max_card = max(numbers)
            for hand in hands:
                max_hand = max(card._rank._number for card in hand._cards)
                if max_hand == max_card:
                    highest_hands.append(hand)
            if len(highest_hands) > 1:
                myset = set()
                for hand in hands:
                    for card in hand._cards:
                        myset.add(card._rank._number)
                cards = list(myset)
                cards.sort(reverse=True)
                for i in range(len(cards)):
                    max_card = cards[i]
                    count = 0
                    for hand in hands:
                        if hand._cards[i]._rank._number == max_card:
                            count += 1
                        else:
                            highest_hands.remove(hand)
                    if count == 1:
                        hand = next(filter(lambda c: c._cards[i]._rank._number == max_card, hands))
                        return [hand]
            return highest_hands
        if play_type == PlayType.ONE_PAIR:
            max_sum = max(sum(card._rank._number for card in hand._cards[:2]) for hand in hands)
            for hand in hands:
                sum_hand = sum(card._rank._number for card in hand._cards[:2])
                if sum_hand == max_sum:
                    highest_hands.append(hand)
            if len(highest_hands) > 1:
                myset = set()
                for hand in hands:
                    for card in hand._cards[-3:]:
                        myset.add(card._rank._number)
                cards = list(myset)
                cards.sort(reverse=True)
                for i in range(len(cards)):
                    max_card = cards[i]
                    count = 0
                    for hand in hands:
                        other_cards = hand._cards[-3:]
                        if other_cards[i]._rank._number == max_card:
                            count += 1
                        else:
                            highest_hands.remove(hand)
                    if count == 1:
                        hand = next(filter(lambda c: c._cards[i + 2]._rank._number == max_card, hands))
                        return [hand]
            return highest_hands
        if play_type == PlayType.TWO_PAIR:
            highest_hands = hands
            pairs = list([card._rank._number for card in hand._cards[i:i + 2]] for i in range(0, 4, 2) for hand in hands)
            pairs = list(set(tuple(pair) for pair in pairs))
            pairs.sort(reverse=True)
            for i in range(len(pairs)):
                max_pair = list(pairs[i])
                count = 0
                for hand in hands:
                    hand_pair = list([card._rank._number for card in hand._cards[i:i + 2]] for i in range(0, 4, 2))[i]
                    if hand_pair == max_pair:
                        count += 1
                if count == 1:
                    hand = next(filter(lambda c: list([card._rank._number for card in c._cards[i:i + 2]] for i in range(0, 4, 2))[i] == max_pair, hands))
                    return [hand]
            if len(highest_hands) > 1:
                max_card = max((hand._cards[-1]._rank._number) for hand in hands)
                for hand in highest_hands:
                    hand_card = hand._cards[-1]._rank._number
                    if max_card > hand_card:
                        highest_hands.remove(hand)
            return highest_hands
        if play_type == PlayType.THREE_OF_A_KIND:
            max_sum = max(sum(card._rank._number for card in hand._cards[:3]) for hand in hands)
            for hand in hands:
                sum_hand = sum(card._rank._number for card in hand._cards[:3])
                if sum_hand == max_sum:
                    highest_hands.append(hand)
            if len(highest_hands) > 1:
                myset = set()
                for hand in hands:
                    for card in hand._cards:
                        myset.add(card._rank._number)
                cards = list(myset)
                cards.sort(reverse=True)
                for i in range(len(cards)):
                    max_card = cards[i]
                    count = 0
                    for hand in hands:
                        other_cards = hand._cards[-3:]
                        if other_cards[i]._rank._number == max_card:
                            count += 1
                        else:
                            highest_hands.remove(hand)
                    if count == 1:
                        hand = next(filter(lambda c: c._cards[i + 2]._rank._number == max_card, hands))
                        return [hand]
            return highest_hands
        return cls.get_highest_hand_by_total_amount_hand(hands)


