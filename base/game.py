from typing import Callable, Union
from base.actions import Actions
from base.deck import Deck
from base.hand_evaluator import HandEvaluator
from base.player import Player

class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        self.current_bank = 0
        self.current_bid = 0
        self.players = []
        self.callback = None
        
        self.minimal_blind = 0
        self.maximal_blind = 0
        
        self.hand_evaluator = HandEvaluator()
        
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
        self.reset_bet()
            
    def set_callback(self, callback: Callable[[Player, int], Union[Actions, int | None]]) -> None:
        '''Set the callback for the betting round'''
        self.callback = callback
        
    def reset_bet(self) -> None:
        '''Reset the current bet'''
        self.current_bid = 0

    def betting_round(self) -> None:
        '''Start the betting round'''
        players_copied = self.players.copy()
        for player in players_copied:
            callback_result = self.callback(player, self.current_bid)
            action = callback_result[0]
            
            if action == Actions.CHECK:
                print(f"{player.name} checks.")
            
            if action == Actions.FOLD:
                print(f"{player.name} folds. {player.name} has left the game.")
                self.players.remove(player)
                
            elif action == Actions.CALL:
                player.bet(self.current_bid)
                self.current_bank += self.current_bid
                print(f"{player.name} calls. {player.name} adds {self.current_bid} to the bank.")
                
            elif action == Actions.RAISE:
                raise_amount = callback_result[1]
                self.current_bid = player.bet(raise_amount)
                self.current_bank += self.current_bid
                print(f"{player.name} raises. {player.name} raises by {raise_amount}.")
                
            else:
                raise NotImplementedError("Invalid action.")