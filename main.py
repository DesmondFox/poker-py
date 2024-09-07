from base.actions import Actions
from base.game import Game
from base.player import Player

user = Player("User")
user.set_score(1000)

player1 = Player("Player 1")
player1.set_score(1000)

player2 = Player("Player 2")
player2.set_score(1000)

game = Game()
game.add_players([user, player1, player2])


def callback(player, bid):
    print(f"{player.name}'s turn.")
    
    return Actions.CHECK, None


game.set_callback(callback)


if __name__ == "__main__":
    game.start()