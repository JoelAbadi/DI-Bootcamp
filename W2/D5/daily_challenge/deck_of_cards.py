#Exercise 1

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        self.build()  # Rebuild the deck first (optional reset)
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return "No cards left in the deck."
        return self.cards.pop()
if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    print("Dealing 5 cards:")
    for _ in range(5):
        print(deck.deal())

    print(f"\nCards left in deck: {len(deck.cards)}")
