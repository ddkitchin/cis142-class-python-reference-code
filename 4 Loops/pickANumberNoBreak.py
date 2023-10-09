# @copyright Deborah Kitchin

from random import randint
# Guess the number game. You can play as long as you want
keepGoing = True
games = 0  # counts how many games are played
wins = 0  # counts how many gaems are won
while keepGoing:
    games = games + 1
    print("You have 3 tries to guess the number")
    actualNumber=randint(1,10)
    #print(actualNumber) # uncomment to help with testing
    count = 0
    guess = -1 # set to something it can't be
    while count < 3 and guess != actualNumber:
        guess = int(input("Pick a number between 1 and 10 "))
        count += 1
    if guess == actualNumber:
            wins = wins + 1
            print("You win!")
            break
    else:
        print("You lose. The number is ",actualNumber)
    ''' keepGoing is a boolean. I am setting it by asking
    the user for input, converting it to upper, and checking to see if
    that input is equal to Y. When it is Y keepGoing is True, otherwise False.
    boolean equal x == y is the formula '''
    keepGoing=input("Do you want to keep going Y/N ").upper()=="Y"