''' @copyright Deborah Kitchin

Creates function display a welcome statement for a
war game. If the person has a user name it will greet
them with the name; otherwise it will greet them with
a generic welcome.
    
'''
def main():
    print("in main")
    displayWelcome()
    ''' what happens when name is not entered? '''
    displayWelcome(input("Enter name: "))

def displayWelcome(name=""):
    if (len(name) == 0):
        print("W", end="")
    else:
        print(name + ", w",end="")

    print("elcome to War. In this game, you will")
    print("compete against the computer. The winner is")
    print("the higher card.")

main()
