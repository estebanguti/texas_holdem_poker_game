from model.player import Player
from model.croupier import Croupier
from model.pack import Pack
from service.play_hand_service import PlayHandService
from service.winner_hand_service import WinnerHandService


number_players = int(input('Enter number of players: '))

if (number_players > 9):
    raise Exception('The number of players is not valid: ' + str(number_players) + '. The maximum number of players allowed are 9.')
if (number_players < 2):
    raise Exception('The number of players is not valid: ' + str(number_players) + '. The minimum number of players allowed are 2.')

pack = Pack()
croupier = Croupier(pack)
playerHandService = PlayHandService()
players: list[Player] = []

def get_play_hand(player: Player):
    player._play_hand = playerHandService.get_player_hand(player._cards)
    print(f'The player {player._name} has hand:')
    player.show_hand()

for i in range(number_players):
    name = input('Enter name of player ' + str(i) + ': ')
    player = Player(name)
    cards = []
    cards.append(croupier.deal_card())
    cards.append(croupier.deal_card())
    player._cards = cards
    players.append(player)

print('Show initial hands')
for player in players:
    get_play_hand(player)

flop_cards = croupier.flop()
for player in players:
    player._cards.extend(flop_cards)
    get_play_hand(player)

turn_card = croupier.turn()
for player in players:
    player._cards.append(turn_card)
    get_play_hand(player)

river_card = croupier.river()
for player in players:
    player._cards.append(river_card)
    get_play_hand(player)

winner_players = WinnerHandService().get_winner_players(players)

if len(winner_players) > 1:
    print("It's a tie")
    print('The winners are: ')
    for player in winner_players:
        print(f'{player._name} with hand {player._play_hand}')
else:
    print(f'The winner is: {winner_players[0]._name} with hand {winner_players[0]._play_hand}')
