#@copyright Deborah Kitchin

def main():
    roster = ["Nathan", "Nancy", "Amber", "Aricke", "Dylan", "Jeffery", "AJ"]

    # Add item to end of list
    roster.append("Kelsey")
    print(roster)

    # Add item to specific place in list
    roster.insert(3, "Adrian")
    print(roster)

    # Find item in list
    student = input("Enter a student name ")
    if student in roster:
        print(f"{student} is in class")
        #print name with student number which is 1 plus the index.
        print(f"{student}'s class number is {roster.index(student) + 1}")
    else:
        print(f"{student} is not in class")

    # Remove specific iitem in list by index (del), by value (remove) and by position (pop)
    print(f'roster {roster}')
    del roster[3]
    print(f'roster after del [3] {roster}')
    roster.remove("Nathan")
    print(f'roster after remove("Nathan") {roster}')
    roster.pop(2)
    print(f'roster after pop(2) {roster}')

    # Sum, min and max
    grades = [90, 95, 85, 75, 65, 100]
    print("grades", grades)

    # notice grades does not change with sum, max and min.
    print("Sum of grades =", sum(grades))
    print("Max of grades =", max(grades))
    print("Min of grades =", min(grades))

    # sort changes the list
    ''' When you do set a list = to another this, it does not create separate copies
    of the list. Each list points to the reference of the same list. For instance:
    uncomment the line below and the last print line in this section'''
    #unsortedGrades = grades   # Both point to (referencing) the same list
    '''Now, Comment line directly above and uncomment line directly below to 
       demonstrate how to create 2 separate lists that are indepedent of each other'''
    #unsortedGrades = grades.copy() # causes second independent list to be created.
    '''results in both variables grades and sortedGrade being sorted'''
    print("grades before sort=", grades)
    grades.sort()
    print("grades after sort=", grades)
    #print("unsortedGrades=",unsortedGrades)

    # Slices
    print("Drop 2 Lowest Grades=", grades[2:len(grades)])

    # Swapping. You have to hold a field so you don't
    # write over it.
    hold=roster[-1]
    roster[-1]=roster[1]
    roster[1]=hold
    print(roster)

if __name__ == "__main__":
    main()