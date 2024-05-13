#@copyright Deborah Kitchin

def main()-> None:
    #Set variable character to a space.
    character = " "
    #Keep going while the variable chacters is not an empty string.
    while character != "":
        # print the ascii value of the the characer entered
        # Notice used " on outside of f-string and ' to put actual ' around the ascii value
        print(f"The ASCII value of '{character}' is {ord(character)}.")
        character = input("Enter a character ")

    #Set asciiValue to 100 to force program into the loop. The value can be anything as long as it is >= 0
    asciiValue = 100
    while asciiValue >= 0:
        # print the charcter value of the the ascii entered
        # Notice used ' on outside of f-string and \' to put actual ' around the ascii value.
        # The \ is an escape character to tell the compiler to treat the value as just a plan
        # character ... not the end of the string.
        print(f'The character value of {str(asciiValue)} is \'{chr(asciiValue)}\'')
        asciiValue = int(input("Enter an ascii value "))

if __name__ == "__main__":
    main()