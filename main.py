from base.actions import Actions
from base.game import Game
from base.player import Player

MINIMAL_BLIND = 10
MAXIMAL_BLIND = 100

user = Player("User")
user.set_score(1000)

player1 = Player("Player 1")
player1.set_score(1000)

player2 = Player("Player 2")
player2.set_score(1000)

game = Game()
game.set_blinds(MINIMAL_BLIND, MAXIMAL_BLIND)
game.add_players([user, player1, player2])


def callback(player: Player, bid: int):
    print(f"---------------------------------")
    print(f"✅ {player.name}'s turn.")
    print(f"💵 {player.name}'s score: {player.score}")
    print(f"💰 Current bank: {game.current_bank}")
    if bid > 0:
        print(f"❗ Bid: {bid}")
    print(f"🃏 {player.name}'s hand: {player.hand}")
    
    can_check = bid == 0
    can_call = bid > 0 and player.score >= bid
    
    while True:
        action = input("Enter an action ({check}{call}raise[e], fold[f]): ".format(
            check="check[c], " if can_check else "",
            call="call[l], " if can_call else ""
            )).lower()
        
        if action == "c":
            return Actions.CHECK, None
        elif action == "l":
            return Actions.CALL, None
        elif action == "e":
            amount = int(input("Enter the amount to raise: "))
            return Actions.RAISE, amount
        elif action == "f":
            return Actions.FOLD, None
        else:
            print("Invalid action. Please try again.")


game.set_callback(callback)


if __name__ == "__main__":
    game.start()