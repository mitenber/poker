from card import Card, Deck, Hand

deck = Deck()
deck.shuffle()

hand = Hand()

deck.move_cards(hand, 5)

print(hand)