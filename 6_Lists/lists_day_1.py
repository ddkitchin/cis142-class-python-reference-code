#@copyright Deborah Kitchin
# Define Lists

values = []  # empty list
print("values=", values)

# list of month numbers --- notice month 1 is index0
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("months=", months)
print ("First month number is", months[0])

# list of students in class
roster = ["Archie", "Nancy", "Amber", "Aricke", "Dylan", "Jeffery", "AJ"]
print("roster", roster)

# list of grades
grades = [90, 95, 85, 75, 65, 100]
print("grades", grades)

# Traverse list 3 ways
print("*" * 20, "Option 1: Go through list", "*" * 20)
for student in roster:
    print(student)
print()

print("*" * 20, "Option 2: Go through list", "*" * 20)
for i in range(len(roster)):
    # end=" " will cause print to stay on same line and put a space after the item printed
    print(roster[i], end=" ")
print()

print("*" * 20, "Option 3: Use enumerate to go through list", "*" * 20)
for studentNumber, studentValue in enumerate(roster):
    print(studentNumber, studentValue)
print()

# Access specific item in list
print("Print 3rd item:", roster[2])
print("Print last item:", roster[-1])
print("Print first item using last:",roster[-1*len(roster)])


# list of person's favorite things
# The programmer must know the structure of the data to do this.
myFavorites = ["Debbie", "Pink", 8, "Mario"]
yourFavorites = ["Barbra", "Blue", 24, "GTA"]

# Access list of various things
print("List of various things:",end="")
print(f"{myFavorites[0]}'s favorite color is {myFavorites[1]}, favorite number is {myFavorites[2]}, and favorite character {myFavorites[3]}.")
print(f"{yourFavorites[0]}'s favorite color is {yourFavorites[1]}, favorite number is {yourFavorites[2]}, and favorite character {yourFavorites[3]}.")

# Concatinate 2 list
allFavorites = myFavorites + yourFavorites
print(allFavorites)
