#Alyce Gaines
#CSI261
#Deck of Cards

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    def __init__(self):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.reset()

    def reset(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()

    def count(self):
        return len(self.deck)

print("welcome to the card dealer.")
print("this deck has 52 cards.")

# Create a deck
deck = Deck()

# Shuffle the deck
deck.shuffle()

num_cards_to_deal = int(input("pick a number of cards to deal: "))
dealt_cards = []

for _ in range(num_cards_to_deal):
    card = deck.deal()
    if card is not None:
        dealt_cards.append(f"{card.rank} of {card.suit}")
    else:
        print("all gone!")

if dealt_cards:
    print("dealt cards:")
    for card in dealt_cards:
        print(card)

remaining_count = deck.count()
print(f"remaining cards in the deck: {remaining_count}")

print("may the odds be ever in your favor!")