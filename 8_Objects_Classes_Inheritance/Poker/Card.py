# This module contains code from
# Think Python by Allen B. Downey
# http://thinkpython.com
# Copyright 2012 Allen B. Downey
# License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

class Card:

    def __init__(self, suit=0, rank=2):

        self._suit = suit
        self._rank = rank

        #    Represents a standard playing card.
        #    Attributes:
        #      suit: integer 0-3
        #      rank: integer 1-13
        self._suitNames = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self._rankNames = [None, "Ace", "2", "3", "4", "5", "6", "7",
                     "8", "9", "10", "Jack", "Queen", "King"]

    def getSuit(self):
        return self._suit

    def getRank(self):
        return self._rank

    def __str__(self):
        #       Returns a human-readable string representation.
        return f'{self._rankNames[self._rank]} of {self._suitNames[self._suit]}'

    def __lt__(self, other):
        return (self._suit, self._rank) < (other._suit, other._rank)