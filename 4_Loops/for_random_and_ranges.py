#@copyright Deborah Kitchin

'''Don't confuse the for loop range(start,end) with the
randint(start,end) results.

The for loop range(0,MAX_NUMBERS) stops before the 
limit, in this case MAX_NUMBERS, stops at 4 not 5. 

The randint function(0,MAX_NUMBERS), stops at 5.'''

from random import *
MAX_NUMBERS = 5
def main():
    print("Random Reals")
    for i in range (MAX_NUMBERS):
        print("Iteration=",i,end="")
        randomValue = random()
        print(" Random Value =",randomValue)
    print("Random Integers")
    for i in range (MAX_NUMBERS):
        print("Iteration=",i,end="")
        randomValue = randint(0,MAX_NUMBERS)
        print(" Random Value =",randomValue)

if __name__ == "__main__":
    main()