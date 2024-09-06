from base.deck import Deck
from base.game import Game
from base.player import Player

deck = Deck()
deck.shuffle()

user = Player("User")
user.set_score(1000)

player1 = Player("Player 1")
player1.set_score(1000)

player2 = Player("Player 2")
player2.set_score(1000)

game = Game()
game.add_players([user, player1, player2])

game.start()
