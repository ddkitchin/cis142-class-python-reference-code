#@copyright Deborah Kitchin
from random import randint

''' Demontration of lists used to make a table. The
table represents the class seating assignments. 

Notice there are two variables row and column. They 
are used for 2 different objectives. First, figuring out
how many students in class and the winner use row and
column for the table of columns for the row and the
actual value of the column. In the actual game play
row and column are used as indexes. '''

EMPTY=9
# Replace EMPTY in the table with student name.
students=[[EMPTY,EMPTY,EMPTY,EMPTY,"Thor",EMPTY],
          [EMPTY,EMPTY,"Black Panther",EMPTY,EMPTY,EMPTY],
          ["Hulk",EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
          [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]]

def main()-> None:
    count=calculateStudents()
    playGame(count)
    showWinner()

# Figure out how many students in class
def calculateStudents()-> int:
    count=0
    for row in students:
        for column in row:
            if column != EMPTY:
                count += 1
    return count

# Play the Last Person Standing Game
def playGame(count:int)-> None:
    while input("Class, please stand up. Enter Y when class is standing. ").upper() != "Y":
        print("Let's go")
    while (count > 1):
        found=False
        while not found:
            row = randint(0,len(students)-1)
            column = randint(0,len(students[0])-1)
            if students[row][column] != EMPTY:
                count -= 1
                print(f'{students[row][column]} please sit down.')
                if count != 1:
                    while input(f"Thank you {students[row][column]}. Enter Y if you are ready to continue. ").upper() != "Y":
                        print("Let's go")
                students[row][column]=EMPTY
                found=True
                    
# Show the winner.
def showWinner()-> None:
    for row in students:
        for column in row:
            if column != EMPTY:
                print(f"{column} you won. YEAH!!!! Please sit down.")
            
if __name__ == "__main__":
    main()