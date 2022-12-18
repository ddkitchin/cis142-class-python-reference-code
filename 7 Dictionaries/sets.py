#@copyright Deborah Kitchin
game102Class=set()
pythonClass=set()

moreStudents=True
while moreStudents:
    studentName=input("Enter a student in game 102 ")
    if studentName != "":
        game102Class.add(studentName)
    else:
        moreStudents=False

moreStudents=True
while moreStudents:
    studentName=input("Enter a student in python ")
    if studentName != "":
        pythonClass.add(studentName)
    else:
        moreStudents=False
    
print("Game class ",game102Class)
print("Python class ",pythonClass)
print("Union ",game102Class.union(pythonClass))
print("Intersection ",game102Class.intersection(pythonClass))
print("Difference",game102Class.difference(pythonClass))