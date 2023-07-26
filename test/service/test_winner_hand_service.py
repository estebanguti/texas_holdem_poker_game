from model.card import Card
from model.enums.play_type import PlayType
from model.play_hand import PlayHand
from service.winner_hand_service import WinnerHandService
from model.enums.rank import Rank


def test_get_winner_hand_by_highest_play_type_hand():
    player1testhand = [Card(Rank.EIGHT, 1), Card(Rank.EIGHT, 4),
                Card(Rank.EIGHT, 3), Card(Rank.ACE, 2),
                Card(Rank.QUEEN, 1)]
    
    player2testhand = [Card(Rank.QUEEN, 4), Card(Rank.QUEEN, 1),
                Card(Rank.EIGHT, 4), Card(Rank.EIGHT, 3),
                Card(Rank.ACE, 2)]
    
    play_hand1 = PlayHand(PlayType.THREE_OF_A_KIND, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_winner_hand_by_high_card_hand():
    player1testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 3),
                Card(Rank.QUEEN, 4), Card(Rank.JACK, 3),
                Card(Rank.EIGHT, 4)]
    
    player2testhand = [Card(Rank.KING, 1), Card(Rank.QUEEN, 4),
                Card(Rank.EIGHT, 4), Card(Rank.SEVEN, 3),
                Card(Rank.QUEEN, 4)]
    
    play_hand1 = PlayHand(PlayType.HIGH_CARD, player1testhand)
    play_hand2 = PlayHand(PlayType.HIGH_CARD, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_winner_hand_by_high_card_hand_second_kicker():
    player1testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 4),
                Card(Rank.TEN, 3), Card(Rank.EIGHT, 4),
                Card(Rank.SEVEN, 1)]
    
    player2testhand = [Card(Rank.ACE, 4), Card(Rank.QUEEN, 4),
                Card(Rank.JACK, 3), Card(Rank.NINE, 2),
                Card(Rank.EIGHT, 4)]
    
    play_hand1 = PlayHand(PlayType.HIGH_CARD, player1testhand)
    play_hand2 = PlayHand(PlayType.HIGH_CARD, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_winner_hand_by_high_card_hand_third_kicker():
    player1testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 4),
                Card(Rank.TEN, 3), Card(Rank.EIGHT, 4),
                Card(Rank.SEVEN, 1)]
    
    player2testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 4),
                Card(Rank.JACK, 3), Card(Rank.NINE, 2),
                Card(Rank.EIGHT, 4)]
    
    play_hand1 = PlayHand(PlayType.HIGH_CARD, player1testhand)
    play_hand2 = PlayHand(PlayType.HIGH_CARD, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand2]

def test_get_winner_hand_by_high_card_hand_fourth_kicker():
    player1testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 4),
                Card(Rank.JACK, 3), Card(Rank.EIGHT, 4),
                Card(Rank.SEVEN, 1)]
    
    player2testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 4),
                Card(Rank.JACK, 3), Card(Rank.NINE, 2),
                Card(Rank.EIGHT, 4)]
    
    play_hand1 = PlayHand(PlayType.HIGH_CARD, player1testhand)
    play_hand2 = PlayHand(PlayType.HIGH_CARD, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand2]

def test_get_winner_hand_by_high_card_hand_fifth_kicker():
    player1testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 4),
                Card(Rank.JACK, 3), Card(Rank.EIGHT, 4),
                Card(Rank.SEVEN, 1)]
    
    player2testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 4),
                Card(Rank.JACK, 3), Card(Rank.EIGHT, 2),
                Card(Rank.TWO, 4)]
    
    play_hand1 = PlayHand(PlayType.HIGH_CARD, player1testhand)
    play_hand2 = PlayHand(PlayType.HIGH_CARD, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_tie_by_high_card_hand():
    player1testhand = [Card(Rank.ACE, 4), Card(Rank.KING, 4),
                Card(Rank.JACK, 3), Card(Rank.EIGHT, 4),
                Card(Rank.SEVEN, 1)]
    
    player2testhand = [Card(Rank.ACE, 3), Card(Rank.KING, 4),
                Card(Rank.JACK, 3), Card(Rank.EIGHT, 4),
                Card(Rank.SEVEN, 1)]
    
    play_hand1 = PlayHand(PlayType.HIGH_CARD, player1testhand)
    play_hand2 = PlayHand(PlayType.HIGH_CARD, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1, play_hand2]

def test_get_winner_hand_by_highest_one_pair_hand_first_kicker():
    player1testhand = [Card(Rank.FOUR, 2), Card(Rank.FOUR, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.FOUR, 2), Card(Rank.FOUR, 4),
                Card(Rank.QUEEN, 2), Card(Rank.JACK, 4),
                Card(Rank.TEN, 3)]
    
    play_hand1 = PlayHand(PlayType.ONE_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.ONE_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_winner_hand_by_highest_one_pair_hand_second_kicker():
    player1testhand = [Card(Rank.FOUR, 2), Card(Rank.FOUR, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.FOUR, 2), Card(Rank.FOUR, 4),
                Card(Rank.ACE, 4), Card(Rank.JACK, 4),
                Card(Rank.TEN, 3)]
    
    play_hand1 = PlayHand(PlayType.ONE_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.ONE_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand2]

def test_get_winner_hand_by_highest_one_pair_hand_third_kicker():
    player1testhand = [Card(Rank.FOUR, 2), Card(Rank.FOUR, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.FOUR, 2), Card(Rank.FOUR, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.NINE, 3)]
    
    play_hand1 = PlayHand(PlayType.ONE_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.ONE_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand2]

def test_get_tie_by_one_pair_hand():
    player1testhand = [Card(Rank.THREE, 2), Card(Rank.THREE, 4),
                Card(Rank.QUEEN, 4), Card(Rank.JACK, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.THREE, 2), Card(Rank.THREE, 4),
                Card(Rank.QUEEN, 4), Card(Rank.JACK, 3),
                Card(Rank.EIGHT, 3)]
    
    play_hand1 = PlayHand(PlayType.ONE_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.ONE_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1,play_hand2]

def test_get_winner_hand_by_highest_two_pair_hand():
    player1testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.FOUR, 4), Card(Rank.FOUR, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.QUEEN, 2), Card(Rank.QUEEN, 4),
                Card(Rank.TEN, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand2]

def test_get_winner_hand_by_highest_two_pair_hand_first_pair():
    player1testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.QUEEN, 4), Card(Rank.QUEEN, 3),
                Card(Rank.TEN, 3)]
    
    player2testhand = [Card(Rank.QUEEN, 4), Card(Rank.QUEEN, 3),
                Card(Rank.JACK, 2), Card(Rank.JACK, 4),
                Card(Rank.TEN, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_winner_hand_by_highest_two_pair_hand_second_pair():
    player1testhand = [Card(Rank.NINE, 2), Card(Rank.NINE, 4),
                Card(Rank.SEVEN, 4), Card(Rank.SEVEN, 3),
                Card(Rank.KING, 3)]
    
    player2testhand = [Card(Rank.NINE, 2), Card(Rank.NINE, 4),
                Card(Rank.EIGHT, 2), Card(Rank.EIGHT, 4),
                Card(Rank.SEVEN, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand2]

def test_get_winner_hand_by_highest_two_pair_hand_kicker():
    player1testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.FOUR, 4), Card(Rank.FOUR, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.FOUR, 4), Card(Rank.FOUR, 3),
                Card(Rank.TEN, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand2]

def test_get_tie_by_two_pairs_hands():
    player1testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.FOUR, 4), Card(Rank.FOUR, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.FOUR, 4), Card(Rank.FOUR, 3),
                Card(Rank.EIGHT, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1,play_hand2]

def test_get_winner_hand_by_highest_three_of_a_kind_hand():
    player1testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.ACE, 4), Card(Rank.FOUR, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.FOUR, 4), Card(Rank.FOUR, 3),
                Card(Rank.FOUR, 2), Card(Rank.ACE, 4),
                Card(Rank.EIGHT, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_winner_hand_by_highest_three_of_a_kind_hand_first_kicker():
    player1testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.ACE, 4), Card(Rank.EIGHT, 3),
                Card(Rank.FIVE, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_winner_hand_by_highest_three_of_a_kind_hand_second_kicker():
    player1testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.FIVE, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1]

def test_get_tie_by_highest_three_of_a_kind_hand():
    player1testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.EIGHT, 3)]
    
    player2testhand = [Card(Rank.ACE, 2), Card(Rank.ACE, 4),
                Card(Rank.ACE, 4), Card(Rank.TEN, 3),
                Card(Rank.EIGHT, 3)]
    
    play_hand1 = PlayHand(PlayType.TWO_PAIR, player1testhand)
    play_hand2 = PlayHand(PlayType.TWO_PAIR, player2testhand)
    winner_hand_service = WinnerHandService()

    assert winner_hand_service.get_winner_hand([play_hand1,play_hand2]) == [play_hand1, play_hand2]