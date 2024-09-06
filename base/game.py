from base.deck import Deck
from base.player import Player

class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
    
    def add_players(self, players: list[Player]) -> None:
        self.players = players
        
    def start(self) -> None:
        for p in self.players:
            p.receive_cards(self.deck.deal())
            print(f"Preflop: {p}")