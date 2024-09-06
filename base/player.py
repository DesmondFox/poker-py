from base.card import Card

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.current_bet = 0
        
    def __repr__(self) -> str:
        return f"{self.name}: [{self.cards[0]}, {self.cards[1]}], score: {self.score}"
        
    def receive_cards(self, cards: list[Card]):
        self.cards = cards
        
    def set_score(self, score: int):
        self.score = score
        
    def bet(self, amount: int):
        if amount > self.score:
            print(f"{self.name} does not have enough money to bet {amount}.")
        else:
            self.score -= amount
            self.current_bet += amount
            print(f"{self.name} bets {amount}.")
    
    