# This module contains code from
# Think Python by Allen B. Downey
# http://thinkpython.com
# Copyright 2012 Allen B. Downey
# License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
from Deck import Deck


class Hand(Deck):
    #   Represents a hand of playing cards.

    def __init__(self, label=''):
        self._cards = []
        self._label = label
