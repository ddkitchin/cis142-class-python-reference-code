# This module contains code from
# Think Python by Allen B. Downey
# http://thinkpython.com
# Copyright 2012 Allen B. Downey
# License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
from PokerHand import PokerHand
from Deck import Deck
from Hand import Hand

def findDefiningClass(obj, methodName):
    #   Finds and returns the class object that will provide
    #   the definition of method_name (as a string) if it is
    #   invoked on obj.
    #   obj: any python object
    #   method_name: string method name
    for ty in type(obj).mro():
        if methodName in ty.__dict__:
            return ty
    return None

def main():

    deck = Deck()
    deck.shuffle() # comment this out to test a straight flush

    hand = Hand()
    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.moveCards(hand, 7)
        hand.sort()
        print(hand)
        hand.createRankHistogram()
        hand.createSuitHistogram()
        if hand.hasFlush():
            print("================Flush")
        else:
            print("================You got to know when to fold em")

if __name__ == "__main__":
    main()