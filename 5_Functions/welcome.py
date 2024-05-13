''' @copyright Deborah Kitchin

Creates function display a welcome statement for a
war game. If the person has a user name it will greet
them with the name; otherwise it will greet them with
a generic welcome.
    
'''
def main()-> None:
    print("in main")
    displayWelcome()
    ''' what happens when name is not entered? '''
    displayWelcome(input("Enter name: "))

def displayWelcome(name:str="")-> None:
    if (len(name) == 0):
        print(f"W",end="")
    else:
        print(f'{name}, w',end="")

    print(f"elcome to War. In this game, you will")
    print(f"compete against the computer. The winner is")
    print(f"the higher card.")

if __name__ == "__main__":
    main()