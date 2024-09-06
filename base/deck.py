import random
from base.card import Card
from base.rank import Rank
from base.suit import Suit

class Deck:
    def __init__(self) -> None:
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]
        
    def shuffle(self) -> None:
        random.shuffle(self.cards)
        
    def deal(self) -> list[Card]:
        return [self.cards.pop() for _ in range(2)]