from model.card import Card
from model.enums.play_type import PlayType
from model.enums.rank import Rank
from service.play_hand_service import PlayHandService

def test_one_pair():
    testhand = [Card(Rank.TWO, 4), Card(Rank.FIVE, 3),
                Card(Rank.THREE, 2), Card(Rank.ACE, 3),
                Card(Rank.TWO, 1)]
    
    playerHand = PlayHandService()

    assert playerHand.has_one_pair(testhand)

def test_two_pair():
    testhand = [Card(Rank.TWO, 4), Card(Rank.FIVE, 3),
                Card(Rank.THREE, 2), Card(Rank.THREE, 3),
                Card(Rank.TWO, 1)]

    playerHand = PlayHandService()

    assert playerHand.has_two_pair(testhand)

def test_three_pair():
    testhand = [Card(Rank.FIVE, 4), Card(Rank.FIVE, 3),
                Card(Rank.FIVE, 2), Card(Rank.ACE, 3),
                Card(Rank.TWO, 1)]

    playerHand = PlayHandService()

    assert playerHand.has_three_of_a_kind(testhand)

def test_straight():
    testhand = [Card(Rank.KING, 4), Card(Rank.QUEEN, 3),
                Card(Rank.JACK, 2), Card(Rank.TEN, 2),
                Card(Rank.NINE, 2)]

    playerHand = PlayHandService()

    assert playerHand.has_straight(testhand)

def test_has_straight_low_ace():
    ace = Card(Rank.ACE, 4)
    three = Card(Rank.THREE, 3)
    jack = Card(Rank.JACK, 2)
    four = Card(Rank.FOUR, 2)
    five = Card(Rank.FIVE, 2)
    testhand = [jack, four,
                five, Card(Rank.TWO, 3),
                ace, three,
                Card(Rank.SEVEN, 3)]

    playerHand = PlayHandService()

    assert playerHand.has_straight(testhand)

def test_flush():
    testhand = [Card(Rank.ACE, 4), Card(Rank.FOUR, 4),
                Card(Rank.NINE, 4), Card(Rank.JACK, 4),
                Card(Rank.TWO, 4)]

    playerHand = PlayHandService()

    assert playerHand.has_flush(testhand)

def test_poker():
    testhand = [Card(Rank.FIVE, 4), Card(Rank.FIVE, 3),
                Card(Rank.FIVE, 2), Card(Rank.FIVE, 1),
                Card(Rank.TWO, 1)]

    playerHand = PlayHandService()

    assert playerHand.has_poker(testhand)

def test_full_house():
    testhand = [Card(Rank.FIVE, 4), Card(Rank.FIVE, 3),
                Card(Rank.FIVE, 2), Card(Rank.TWO, 3),
                Card(Rank.TWO, 1)]

    playerHand = PlayHandService()

    assert playerHand.has_full_house(testhand)

def test_straight_flush():
    testhand = [Card(Rank.TEN, 1), Card(Rank.SEVEN, 1),
                Card(Rank.NINE, 1), Card(Rank.SIX, 1),
                Card(Rank.EIGHT, 1)]

    playerHand = PlayHandService()

    assert playerHand.has_straight_flush(testhand)

def test_royal_flush():
    testhand = [Card(Rank.ACE, 3), Card(Rank.JACK, 3),
                Card(Rank.KING, 3), Card(Rank.TEN, 3),
                Card(Rank.QUEEN, 3)]

    playerHand = PlayHandService()

    assert playerHand.has_royal_flush(testhand)


def test_order_by_highest_cards():
    ace = Card(Rank.ACE, 3)
    jack = Card(Rank.JACK, 4)
    eight = Card(Rank.EIGHT, 1)
    six = Card(Rank.SIX, 3)
    five = Card(Rank.FIVE, 3)
    testhand = [jack, five,
                Card(Rank.THREE, 2), ace,
                eight, Card(Rank.TWO, 3),
                six]
    
    playerHand = PlayHandService()

    assert playerHand.order_by_highest_cards(testhand) == [ace, jack, eight, six, five]

def test_get_one_pair_hand():
    ace = Card(Rank.ACE, 3)
    ace2 = Card(Rank.ACE, 4)
    eight = Card(Rank.EIGHT, 1)
    six = Card(Rank.SIX, 3)
    five = Card(Rank.FIVE, 3)
    testhand = [ace2, five,
                Card(Rank.THREE, 2), ace,
                eight, Card(Rank.TWO, 3),
                six]
    
    playerHand = PlayHandService()

    assert playerHand.get_one_pair_hand(testhand) == [ace2, ace, eight, six, five]

def test_get_two_pair_hand():
    ace = Card(Rank.ACE, 3)
    ace2 = Card(Rank.ACE, 4)
    eight = Card(Rank.EIGHT, 1)
    eight2 = Card(Rank.EIGHT, 3)
    five = Card(Rank.FIVE, 3)
    five2 = Card(Rank.FIVE, 2)
    testhand = [ace2, five,
                five2, ace,
                eight, Card(Rank.TWO, 3),
                eight2]
    
    playerHand = PlayHandService()

    assert playerHand.get_two_pair_hand(testhand) == [ace2, ace, eight, eight2, five]

def test_get_three_of_a_kind_hand():
    ace = Card(Rank.ACE, 3)
    ace2 = Card(Rank.ACE, 4)
    ace3 = Card(Rank.ACE, 1)
    eight = Card(Rank.EIGHT, 3)
    five = Card(Rank.FIVE, 3)
    jack = Card(Rank.JACK, 2)
    testhand = [ace2, five,
                jack, ace,
                eight, Card(Rank.TWO, 3),
                ace3]
    
    playerHand = PlayHandService()

    assert playerHand.get_three_of_a_kind_hand(testhand) == [ace2, ace, ace3, jack, eight]

def test_get_straight_hand():
    nine = Card(Rank.NINE, 3)
    eight = Card(Rank.EIGHT, 4)
    seven = Card(Rank.SEVEN, 1)
    six = Card(Rank.SIX, 3)
    five = Card(Rank.FIVE, 3)
    four = Card(Rank.FOUR, 2)
    testhand = [six, five,
                four, nine,
                eight, seven,
                Card(Rank.SEVEN, 3)]
    
    playerHand = PlayHandService()

    assert playerHand.get_straight_hand(testhand) == [nine, eight, seven, six, five]

def test_get_straight_hand_low_ace():
    ace = Card(Rank.ACE, 4)
    three = Card(Rank.THREE, 3)
    jack = Card(Rank.JACK, 2)
    four = Card(Rank.FOUR, 2)
    five = Card(Rank.FIVE, 2)
    two = Card(Rank.TWO, 3)
    testhand = [jack, four,
                five, two,
                ace, three,
                Card(Rank.SEVEN, 3)]
    
    playerHand = PlayHandService()

    assert playerHand.get_straight_hand(testhand) == [five, four, three, two, ace]

def test_get_straight_high_ace_hand():
    ace = Card(Rank.ACE, 4)
    king = Card(Rank.KING, 4)
    queen = Card(Rank.QUEEN, 3)
    jack = Card(Rank.JACK, 2)
    ten = Card(Rank.TEN, 2)
    nine = Card(Rank.NINE, 2)
    testhand = [jack, ten,
                nine, Card(Rank.TWO, 3),
                king, queen,
                Card(Rank.SEVEN, 3), ace]

    playerHand = PlayHandService()

    assert playerHand.get_straight_hand(testhand) == [ace, king, queen, jack, ten]

def test_get_flush_hand():
    ace = Card(Rank.ACE, 2)
    queen = Card(Rank.QUEEN, 2)
    ten = Card(Rank.TEN, 2)
    six = Card(Rank.SIX, 2)
    two = Card(Rank.TWO, 3)
    jack = Card(Rank.JACK, 2)
    testhand = [queen, six,
                jack, ace,
                two, Card(Rank.TWO, 3),
                ten]
    
    playerHand = PlayHandService()

    assert playerHand.get_flush_hand(testhand) == [ace, queen, jack, ten, six]

def test_get_full_house_hand():
    ace = Card(Rank.ACE, 2)
    ace2 = Card(Rank.ACE, 1)
    ace3 = Card(Rank.ACE, 4)
    six = Card(Rank.SIX, 2)
    six2 = Card(Rank.SIX, 3)
    jack = Card(Rank.JACK, 2)
    jack2 = Card(Rank.JACK, 1)
    testhand = [ace, ace2,
                jack, ace3,
                six2, jack2,
                six]
    
    playerHand = PlayHandService()

    assert playerHand.get_full_house_hand(testhand) == [ace, ace2, ace3, jack, jack2]

def test_get_best_full_house_play_hand():
    play_type = PlayType.FULL_HOUSE
    ace1 = Card(Rank.ACE, 3)
    ace2 = Card(Rank.ACE, 4)
    ace3 = Card(Rank.ACE, 1)
    king1 = Card(Rank.KING, 4)
    king2 = Card(Rank.KING, 2)
    king3 = Card(Rank.KING, 3)
    testhand = [ace3, king1,
                king2, Card(Rank.FOUR, 4),
                ace1, ace2,
                king3]

    playerHand = PlayHandService()
    play_hand = playerHand.get_player_hand(testhand)

    assert play_hand._play_type == play_type and play_hand._cards == [ace3, ace1, ace2, king1, king2]

def test_get_full_house_play_hand_by_higesth_two_pair():
    play_type = PlayType.FULL_HOUSE
    two1 = Card(Rank.TWO, 3)
    two2 = Card(Rank.TWO, 4)
    two3 = Card(Rank.TWO, 1)
    five1 = Card(Rank.FIVE, 4)
    eight1 = Card(Rank.EIGHT, 2)
    eight2 = Card(Rank.EIGHT, 3)
    testhand = [two3, five1,
                eight1, Card(Rank.FIVE, 3),
                two1, two2,
                eight2]

    playerHand = PlayHandService()
    play_hand = playerHand.get_player_hand(testhand)

    assert play_hand._play_type == play_type and play_hand._cards == [two3, two1, two2, eight1, eight2]

def test_get_poker_hand():
    ace = Card(Rank.ACE, 3)
    ace2 = Card(Rank.ACE, 4)
    ace3 = Card(Rank.ACE, 1)
    ace4 = Card(Rank.ACE, 2)
    five = Card(Rank.FIVE, 3)
    jack = Card(Rank.JACK, 2)
    testhand = [ace2, five,
                jack, ace,
                ace4, Card(Rank.TWO, 3),
                ace3]
    
    playerHand = PlayHandService()

    assert playerHand.get_poker_hand(testhand) == [ace2, ace, ace4, ace3, jack]

def test_get_straight_flush_hand():
    nine = Card(Rank.NINE, 1)
    eight = Card(Rank.EIGHT, 1)
    seven = Card(Rank.SEVEN, 1)
    six = Card(Rank.SIX, 1)
    five = Card(Rank.FIVE, 1)
    four = Card(Rank.FOUR, 1)
    testhand = [six, five,
                four, nine,
                eight, seven,
                Card(Rank.SEVEN, 3)]
    
    playerHand = PlayHandService()

    assert playerHand.get_straight_flush_hand(testhand) == [nine, eight, seven, six, five]

def test_get_straight_flush_hand_low_ace():
    ace = Card(Rank.ACE, 4)
    three = Card(Rank.THREE, 4)
    jack = Card(Rank.JACK, 4)
    four = Card(Rank.FOUR, 4)
    five = Card(Rank.FIVE, 4)
    two = Card(Rank.TWO, 4)
    testhand = [jack, four,
                five, two,
                ace, three,
                Card(Rank.SEVEN, 3)]
    
    playerHand = PlayHandService()

    assert playerHand.get_straight_flush_hand(testhand) == [five, four, three, two, ace]
    
def test_get_royal_flush_hand():
    ace = Card(Rank.ACE, 4)
    king = Card(Rank.KING, 4)
    queen = Card(Rank.QUEEN, 4)
    jack = Card(Rank.JACK, 4)
    ten = Card(Rank.TEN, 4)
    nine = Card(Rank.NINE, 4)
    testhand = [jack, ten,
                nine, ace,
                king, queen,
                Card(Rank.SEVEN, 3)]
    
    playerHand = PlayHandService()

    assert playerHand.get_royal_flush_hand(testhand) == [ace, king, queen, jack, ten]

