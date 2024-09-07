from base.card import Card

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.current_bet = 0
        self.hand = []
        
    def __repr__(self) -> str:
        return f"{self.name}: [{self.hand[0]}, {self.hand[1]}], score: {self.score}"
        
    def receive_cards(self, cards: list[Card]):
        '''Receive cards from the deck to the player\'s hand'''
        self.hand = cards
        
    def set_score(self, score: int):
        '''Set the player\'s score'''
        self.score = score
        
    def bet(self, amount: int) -> int:
        '''Place a bet'''
        if amount > self.score:
            print(f"{self.name} does not have enough money to bet {amount}.")
            
            return 0
        else:
            self.score -= amount
            self.current_bet += amount
            print(f"{self.name} bets {amount}.")
            
            return amount
    
    