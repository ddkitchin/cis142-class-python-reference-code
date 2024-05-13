#@copyright Deborah Kitchin
# create error when number entered is not between 0 and 100.
class CustomGradeRangeError(Exception):
   pass

def main()-> None:
   enterGrades()

def enterGrades()-> None:
   count = 0
   # infinite loop that breaks when count = 10
   while True:
      count += 1
      if count > 10:
         break
      
      # Try used to mark where you could want to watch for errors.
      try:
         mark = int(input("Please enter the exam mark out of 100 "))
         # get to next line when mark is numeric
         if mark in range(0, 101):
            print(f"Your mark is {mark}.")
         else:
            # raise custom exception when number is not between 0 and 10
            raise CustomGradeRangeError
         # only get here when line 21 is executed
         print(f"{count} after if else")

      # only get here when an exception is raised
      except ValueError:
         print(f"\nPlease only use integers")
      except CustomGradeRangeError:
         print(f"\nPlease enter a number between 0 and 100")

if __name__ == "__main__":
    main()