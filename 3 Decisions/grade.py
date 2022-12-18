#@copyright Deborah Kitchin

#set real variable score to the user input
score = float(input("Enter score: "))

if score >= 59.5:
    print("You passed")
else:
    print("You failed")