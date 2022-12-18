# This module contains code from
# Think Python by Allen B. Downey
# http://thinkpython.com
# Copyright 2012 Allen B. Downey
# License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

import random
from card import Card


class Deck:
    #    Represents a deck of cards.
    #    Attributes:
    #     cards: list of Card objects.

    def __init__(self):
        self._cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self._cards.append(card)

    def __str__(self):
        res = []
        for card in self._cards:
            res.append(str(card))
        return '\n'.join(res)

    def addCard(self, card):
        self._cards.append(card)

    def removeCard(self, card):
        self._cards.remove(card)

    def popCard(self, i=-1):
        #       Removes and returns a card from the deck.
        #       i: index of the card to pop; by default, pops the last card.
        return self._cards.pop(i)

    def shuffle(self):
        random.shuffle(self._cards)

    def sort(self):
        #       Sorts the cards by suit then rank
        self._cards.sort()

    def moveCards(self, hand, num):
        #        Moves the given number of cards from the deck into the Hand.
        for i in range(num):
            hand.addCard(self.popCard())
