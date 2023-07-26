from collections import Counter
import math

from service.play_hand_service import PlayHandService

# TO DO: Calculate Odds for play hands
class PokerCalculation:

    _play_hand_service = PlayHandService()

    def combinations(cls, n,k):
        all_posibilities = float(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
        return all_posibilities
    
    def calculate_probability(cls, frequency):
        all_posibilities = cls.combinations(52,5)
        return (frequency / all_posibilities) * 100
    
    def calculate_probability_2(cls, frequency, cards):
        all_posibilities = cls.combinations(cards, 5)
        return (frequency / all_posibilities) * 100
    
    def calculate_probability_3(cls, deck, num_out_comes):
        return (1 - ((len(deck) - num_out_comes) / len(deck))) * 100
    
    def event_probability(event_outcomes, sample_space):
        probability = (event_outcomes / sample_space) * 100
        return round(probability, 1)
    
    def poker_probabilities(cls):
        royal_flush_frequency = cls.combinations(4,1)
        royal_flush_probability = cls.calculate_probability(royal_flush_frequency)
        straight_flush_frequency = cls.combinations(4,1) * cls.combinations(9,1)
        straight_flush_probability = cls.calculate_probability(straight_flush_frequency)
        four_of_a_kind_frequency = cls.combinations(13,1) * cls.combinations(13-1,1) * cls.combinations(4,1) #Available 13 cards, also 12 possibilities for the fifth one and 4 colors
        four_of_a_kind_probability = cls.calculate_probability(four_of_a_kind_frequency)
        full_house_frequency = cls.combinations(13,1) * cls.combinations(4,3) * cls.combinations(13-1,1) * cls.combinations(4,2) #We have first three: 13 cards, 4 posibilities, last two: 12 cards, 6 posibilities
        full_house_probability = cls.calculate_probability(full_house_frequency)
        flush_frequency = (cls.combinations(13,5) * cls.combinations(4,1) - royal_flush_frequency - straight_flush_frequency)
        flush = cls.calculate_probability(flush_frequency)
        straight_frequency = cls.combinations(10,1) * 4**5 - straight_flush_frequency # 10 possible sequences are there,and also 4 choices from all the colours
        straight_probability = cls.calculate_probability(straight_frequency)
        three_of_a_kind_frequency = cls.combinations(13,1) * cls.combinations(4,3) * cls.combinations(13-1,2) * 4**2  # Available 13 cards, 4 posibilities,we need to choose 2 from 12 cards,
        three_of_a_kind_probability = cls.calculate_probability(three_of_a_kind_frequency)
        two_pair_frequency = cls.combinations(13,2) * cls.combinations(4,2)**2 * cls.combinations(13-2,1) * cls.combinations(4,1) # 2 pairs and the fifth card not from a pair
        two_pair_probability = cls.calculate_probability(two_pair_frequency)
        one_pair_frequency = cls.combinations(13,1) * cls.combinations(4,2) * cls.combinations(12,3)* cls.combinations(4,1)**3 # 1 pair and three random cards without the one in the pair
        one_pair_probability = cls.calculate_probability(one_pair_frequency)
        no_pair_frequency = (cls.combinations(13,5) - 10) * (cls.combinations(4,1)**5-4) # no pair
        no_pair_probability = cls.calculate_probability(no_pair_frequency)

    def calculate_probabilities_for_hands(cls, hand_cards, deck):
        print('Probability One Pair: ' + str(cls.probability_one_pair(hand_cards, deck)))
        print('Probability Two Pair: ' + str(cls.probability_two_pairs(hand_cards, deck)))
        print('Probability Three of a kind: ' + str(cls.probability_three_of_a_kind(hand_cards, deck)))
        print('Probability Straight: ' + str(cls.probability_straight(hand_cards, deck)))
        print('Probability Flush: ' + str(cls.probability_flush(hand_cards, deck)))
        print('Probability Full House: ' + str(cls.probability_full_house(hand_cards, deck)))
        print('Probability Poker: ' + str(cls.probability_poker(hand_cards, deck)))
        print('Probability Straight Flush: ' + str(cls.probability_straight_flush(hand_cards, deck)))
        print('Probability Royal Flush: ' + str(cls.probability_royal_flush(hand_cards, deck)))

    def probability_one_pair(cls, hand_cards, deck):
        if (cls._play_hand_service.has_one_pair(hand_cards)):
            return 100.0
        else:
            card_outcomes = []
            for hand in hand_cards:
                for card in deck:
                    if hand._rank._number == card._rank._number:
                        card_outcomes.append(card)
            return cls.calculate_probability_3(deck, len(card_outcomes))
        
    def probability_two_pairs(cls, hand_cards, deck):
        if (cls._play_hand_service.has_two_pair(hand_cards)):
            return 100.0
        else:
            card_outcomes = []
            for hand in hand_cards:
                for card in deck:
                    if hand._rank._number == card._rank._number:
                        card_outcomes.append(card)
            count_outcomes = 0 if len(card_outcomes) < 2 else len(card_outcomes)
            return cls.calculate_probability_3(deck, count_outcomes)
        
    def probability_three_of_a_kind(cls, hand_cards, deck):
        if (cls._play_hand_service.has_three_of_a_kind(hand_cards)):
            return 100.0
        else:
            card_outcomes = []
            for hand in hand_cards:
                cards = []
                for card in deck:
                    if hand._rank._number == card._rank._number:
                        cards.append(card)
                if len(cards) >= 3:
                    card_outcomes.extend(cards)
            return cls.calculate_probability_3(deck, len(card_outcomes))
    
    def probability_straight(cls, hand_cards, deck):
        if (cls._play_hand_service.has_straight(hand_cards)):
            return 100.0
        else:
            data = [card._rank._number for card in hand_cards]
            if (data.__contains__(14)):
                data.append(1)
            data.sort()
            missing_cards = []
            for number in data:
                next = number + 1
                previous = number - 1
                for card in deck:
                    if next == card._rank._number:
                        if next not in data:
                            missing_cards.append(card)
                    if previous == card._rank._number:
                        if previous not in data:
                            missing_cards.append(card)
            count_outcomes = len(missing_cards)
            return cls.calculate_probability_3(deck, count_outcomes)
        
    def probability_flush(cls, hand_cards, deck):
        if (cls._play_hand_service.has_flush(hand_cards)):
            return 100.0
        else:
            cards = hand_cards + deck
            list = [obj._suit for obj in cards]
            count_outcomes = len([k for k,v in Counter(list).items() if v>=5])
            return cls.calculate_probability_3(deck, count_outcomes)
        
    def probability_full_house(cls, hand_cards, deck):
        if (cls._play_hand_service.has_full_house(hand_cards)):
            return 100.0
        else:
            full_house_frequency = cls.combinations(13,1) * cls.combinations(4,3) * cls.combinations(13-1,1) * cls.combinations(4,2) 
            return cls.calculate_probability_2(full_house_frequency, len(deck))
        
    def probability_poker(cls, hand_cards, deck):
        if (cls._play_hand_service.has_poker(hand_cards)):
            return 100.0
        else:
            poker_frequency = cls.combinations(13,1) * cls.combinations(13-1,1) * cls.combinations(4,1)
            return cls.calculate_probability_2(poker_frequency, len(deck))
        
    def probability_straight_flush(cls, hand_cards, deck):
        if (cls._play_hand_service.has_straight_flush(hand_cards)):
            return 100.0
        else:
            straight_flush_frequency = cls.combinations(4,1) * cls.combinations(9,1)
            return cls.calculate_probability_2(straight_flush_frequency, len(deck))
        
    def probability_royal_flush(cls, hand_cards, deck):
        if (cls._play_hand_service.has_royal_flush(hand_cards)):
            return 100.0
        else:
            royal_flush_frequency = cls.combinations(4,1)
            return cls.calculate_probability_2(royal_flush_frequency, len(deck))