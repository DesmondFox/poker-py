from typing import Callable, Union
from base.actions import Actions
from base.deck import Deck
from base.player import Player

class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        self.current_bank = 0
        self.players = []
        self.callback = None
    
    def add_players(self, players: list[Player]) -> None:
        '''Add players'''
        self.players = players
        
    def start(self) -> None:
        '''Start the game, deal initial cards and start the betting'''
        for p in self.players:
            p.receive_cards(self.deck.deal())
            print(f"Initial cards: {p}")
        self.betting_round()
            
    def set_callback(self, callback: Callable[[Player, int], Union[Actions, int | None]]) -> None:
        '''Set the callback for the betting round'''
        self.callback = callback
            
    def betting_round(self) -> None:
        '''Start the betting round'''
        for p in self.players:
            action = self.callback(p, self.current_bank)
            
            if action == Actions.FOLD:
                print(f"{p.name} folds. {p.name} has left the game.")
                self.players.remove(p)
            elif action == Actions.CALL:
                call_amount = self.current_bank - p.current_bet
                p.bet(call_amount)
                print(f"{p.name} calls. {p.name} adds {call_amount} to the bank.")
            elif action == Actions.RAISE:
                raise_amount = action[1]
                p.bet(raise_amount)
                print(f"{p.name} raises. {p.name} raises by {raise_amount}.")
            else:
                print(f"{p.name} checks.")