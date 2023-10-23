#@copyright Deborah Kitchin

def main():
    # Hello World
    print("Hello World")

    ''' Show a variable in a sentence '''
    myName = 'Debbie'
    print(f"The value for the variable name is a portal for {myName}.")

    # Add an age to the sentence
    myAge = 57
    print(f"Hello, My name is {myName} and I'm {myAge} years old.")

    # blank line
    print()

    # Description of Eric Idle
    firstName = "Eric"
    lastName = "Idle"
    age = 74
    profession = "comedian"
    affiliation = "Monty Python"

    # \n will print a blank line after the sentence.
    print(f"Hello, {firstName} {lastName}. You are {age}. You are a {profession}. You were a member of {affiliation}.\n")

    # Calculated values
    print(f"{firstName} is {age - myAge} older than {myName}")

if __name__ == "__main__":
    main()