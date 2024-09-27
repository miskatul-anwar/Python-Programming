import itertools


def main():
    cards = make_deck()
    all_hands = itertools.combinations(cards, 5)
    for hand in all_hands:
        print(hand)
