import random

'''
Students must turn in functions, variables, plan, and flow of all
projects ahead of time. This is graded for good honest effort.
Students will be bad at this. That's ok. I just want them sincerely
trying. You can tell.

Fully implemented deck and card objects.

Students can make poker if they finish blackjack early.
'''

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def print(self):
        print(self.name+' of '+self.suit)


class Deck:
    def __init__(self):
        self.deck = []
        self.drawn = []

    def addCard(self, card):
        self.deck.append(card)

    def shuffle(self):
        '''Shuffle all the drawn cards back into the deck.'''
        self.deck = self.deck + self.drawn
        self.drawn = []
        random.shuffle(self.deck)

    def print(self):
        for card in self.deck:
            card.print()

    def draw(self):
        '''Draw a card.'''
        card = self.deck.pop(0)
        self.drawn.append(card)
        return card


def getDeck():
    #Create deck
    deck = Deck()
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    face_cards = ['jack', 'queen', 'king', 'ace']
    for s in suits:
        for i in range(2,11):
            deck.addCard(Card(str(i), s, i))
        for f in face_cards:
            if f=='ace':
                deck.addCard(Card(f, s, 11))
            else:
                deck.addCard(Card(f, s, 10))
    return deck


def drawHand(deck):
    hand = []
    hand.append(deck.draw())
    hand.append(deck.draw())
    return hand


def getHandValue(hand):
    value = 0
    has_ace = False
    for card in hand:
        if card == 'ace':
            has_ace = True
        value += card.value
    #Use the smaller value of an ace only if it is better
    if value > 21 and has_ace:
        value -= 10
    return value


def printHand(hand):
    for h in hand:
        h.print()


deck = getDeck()
#deck.print()
#print('======================================')
deck.shuffle()

#Testing
#deck.print()
print("Shouldn't there be 56 cards in a deck?")
print(len(deck.deck))

user_choice = ''
while user_choice!='q':
    user_hand = drawHand(deck)
    dealer_hand = drawHand(deck)
    print('Your hand:')
    printHand(user_hand)
    user_choice = input('Hit or stay?')
    while user_choice == 'hit' and getHandValue(user_hand)<21:
        user_hand.append(deck.draw())
        print()
        print('Your hand:')
        printHand(user_hand)
        user_choice = input('Hit or stay?')
    #Dealer strategy:
    while getHandValue(dealer_hand)<12:
        dealer_hand.append(deck.draw())
    #Determine winner
    if getHandValue(user_hand) > 21:
        print('Busted!')
    elif getHandValue(dealer_hand) >= getHandValue(user_hand):
        print('Dealer wins. Dealer\'s hand is')
        printHand(dealer_hand)
    else:
        print('You win!')
        print('Dealer\'s hand is')
        printHand(dealer_hand)
    print()
    user_choice = input('Type q to quit. Anything else to continue.')
