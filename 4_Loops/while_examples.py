#@copyright Deborah Kitchin

def main()-> None:
    # This is an infinite loop if you uncomment it, then your program will
    # continually run lines 4-6. To stop you must kill the program.
    '''while True:
        count += 1
        print("Count ", count)
    '''
    # This while loop uses the break keyword to exit the loop.
    count=0
    while True:
        count+=1
        print("Count ",count)
        if input("Do you want to keep going? Y/N ").upper() == "N":
            print("Goodbye")
            break

    # This while loop uses a signal (keepGoing) and user input to exit the loop.
    print("************** Here we go again *********")
    keepGoing=True
    while keepGoing:
        choice=input("Do you want to keep going? Y/N ")
        if choice.upper() != "Y":
            print("Later")
            keepGoing=False

if __name__ == "__main__":
    main()