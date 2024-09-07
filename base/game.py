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
        
        self.minimal_blind = 0
        self.maximal_blind = 0
        
    def set_blinds(self, minimal_blind: int, maximal_blind: int) -> None:
        '''Set the minimal and maximal blinds'''
        self.minimal_blind = minimal_blind
        self.maximal_blind = maximal_blind
    
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
        for player in self.players:
            callback_result = self.callback(player, self.current_bank)
            action = callback_result[0]
            
            if action == Actions.FOLD:
                print(f"{player.name} folds. {player.name} has left the game.")
                self.players.remove(player)
                
            elif action == Actions.CALL:
                call_amount = self.current_bank - player.current_bet
                player.bet(call_amount)
                print(f"{player.name} calls. {player.name} adds {call_amount} to the bank.")
                
            elif action == Actions.RAISE:
                raise_amount = callback_result[1]
                player.bet(raise_amount)
                print(f"{player.name} raises. {player.name} raises by {raise_amount}.")
                
            else:
                raise NotImplementedError("Invalid action.")