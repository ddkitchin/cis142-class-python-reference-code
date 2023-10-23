#@ copyright Deborah Kitchin

def main():
    # boolean statement and boolean statement
    grade = int(input("Enter grade: "))
    if (grade > 79) and (grade < 90):
        print("B")
    else:
        print("not a B")

    # boolean statement or boolean statement
    passport = input("Enter yes if you have a passport: ")
    driversLicense = input("Enter yes if you have a driver's License: ")
    if (passport == "yes") or (driversLicense == "yes"):
        print("You can fly")
    else:
        print("You can't fly: ")

    # not boolean statement
    done = input("Enter yes when done playing: ")
    if not(done == "yes"):
        print("Keep playing")
    else:
        print("Goodbye")

if __name__ == "__main__":
    main()