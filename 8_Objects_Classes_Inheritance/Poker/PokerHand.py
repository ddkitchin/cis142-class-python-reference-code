# This module contains code from
# Think Python by Allen B. Downey
# http://thinkpython.com
# Copyright 2012 Allen B. Downey
# License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
from Card import Card
from Hand import Hand


class PokerHand(Hand):

    def createSuitHistogram(self):
        #        Builds a histogram of the suits that appear in the hand.
        #        Stores the result in attribute suits.

        self._suits = {}
        for card in self._cards:
            self._suits[card._suit] = self._suits.get(card._suit, 0) + 1

    def createRankHistogram(self):
        #       Builds a histogram of the ranks that appear in the hand.
        #       Stores the result in attribute ranks.

        self._ranks = {}
        for card in self._cards:
            self._ranks[card._rank] = self._ranks.get(card._rank, 0) + 1

    def hasFlush(self):
        for val in self._suits.values():
            if val >= 5:
                return True
        return False
