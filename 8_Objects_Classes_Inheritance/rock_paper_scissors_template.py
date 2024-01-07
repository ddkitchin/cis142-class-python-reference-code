from random import randint


class Hand():

    def __init__():
        # Set name and power to empty string if no parameter is passed using hte parameter in the line above.
        # Set class name to parameter name and classs power to paramter power.
        # Set _wins and _ties ot 0
        print("init")  # remove this when you fix the function.

    def getName():
        # return name
        print('getName')  # remove this when you fix the function.

    def getScore():
        # return the formatted score wth wins and ties.
        print('getScore')  # remove this when you fix the function.

    def winner():
        # add 1 to wins
        print('winner')  # remove this when you fix the function.

    def tie():
        # add 1 to ties
        print('tie')  # remove this when you fix the function.

    def __eq__():
        # check if two objects in the class are the same.
        print('equal')  # remove this when you fix the function.

    def __repr__():
        # Print the fromatted class name and power.
        print('repr')  # remove this when you fix the function.


class Rock(Hand):

    def __init__():
        # set name to Rock and power to breaks
        # call the Hand class init
        print('init')  # remove this when you fix the function.

    def __gt__():
        # check if self wins against other
        print('gt')  # remove this when you fix the function.


class Paper(Hand):

    def __init__():
        # set name to Paper and power to covers
        # call the Hand class init
        print('init')  # remove this when you fix the function.

    def __gt__():
        # check if self wins against other
        print('gt')  # remove this when you fix the function.


class Scissors(Hand):

    def __init__():
        # set name to Scissors and power to cut
        # call the Hand class init
        print('init')  # remove this when you fix the function.

    def __gt__():
        # check if self wins against other
        print('gt')  # remove this when you fix the function.


def main():
    runGame()


def runGame():
    # create a list with a 3 possible hands Rock, Paper, and Scissors objects as items in the list.

    # for i in 100
    #    get an index for the first hand between 0 and 2
    #    get an index for the second hand between 0 and 2
    #    print i plus 1 and stay on the line
    #    if the two hands are the same
    #         print get the first hands name as a tie
    #         call the hands tie function.
    #    else if hand1 is greater than hand 2
    #         print hand1's repr and hand2's getName
    #         call hand1s winner function
    #    else
    #         print hand2's repr and hand2's getName
    #         call hand2s winner function

    # print a break line to show final totals
    # for each hand in hands
    #    print the hand score
    print('runGame')


if __name__ == "__main__":
    main()