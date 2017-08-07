import random

class Card(object):

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def remove_card(self, card):
        self.cards.remove(card)

    def add_card(self, card):
        self.cards.append(card)

    def sort(self):
        self.cards.sort()

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, amount, num):
        hands = [Hand() for h in range(amount)]
        for hand in hands:
            self.move_cards(hand, num)
        return hands


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def pair(self):
        

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hands = deck.deal_hands(3,5)
    count = 0
    for hand in hands:
        count += 1
        print "Hand number ", count
        hand.sort()
        print hand
