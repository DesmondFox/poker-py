from base.suit import Suit
from base.rank import Rank

class Card:
    '''Represents a card'''
    def __init__(self, suit: Suit, rank: Rank) -> None:
        self.suit = suit
        self.rank = rank
        
    def __repr__(self) -> str:
        return f"{self.rank.value[1]}{self.suit.value[1]}"