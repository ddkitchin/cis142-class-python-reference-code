''' Algorithm

get alphanumeric phone number
set newNumber to empty string
for every character in the phone number
    convert alphabetic characters to a number
    append the number to new number
print new number
'''


def main() -> None:
    phoneNumber = input("Enter a phone number: ")
    newNumber = ""

    print("Orignal number", phoneNumber)
    print(newNumber)

    for character in phoneNumber:
        #FIX ME
        #print("not done")
        #print("line 10",character)
        if character.upper() == "A" or character.upper() == "B" or character.upper() == "C":
            newNumber = newNumber + "2"
        elif character.upper() == "D" or character.upper() == "E" or character.upper() == "F":
            newNumber = newNumber + "3"
        elif character.upper() == "G" or character.upper() == "H" or character.upper() == "I":
            newNumber = newNumber + "4"
        elif character.upper() == "J" or character.upper() == "K" or character.upper() == "L":
            newNumber = newNumber + "5"
        elif character.upper() == "M" or character.upper() == "N" or character.upper() == "O":
            newNumber = newNumber + "6"
        elif character.upper() == "P" or character.upper() == "Q" or character.upper() == "R" or character.upper() == "S":
            newNumber = newNumber + "7"
        elif character.upper() == "T" or character.upper() == "U" or character.upper() == "V":
            newNumber = newNumber + "8"
        #else:
        elif character.upper() == "W" or character.upper() == "X" or character.upper() == "Y" or character.upper() == "Z":
            newNumber = newNumber + "9"
        else:
            newNumber = newNumber + character

    print("final new number", newNumber)


if __name__ == "__main__":
    main()
