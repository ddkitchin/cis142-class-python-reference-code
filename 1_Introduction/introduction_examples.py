#@copyright Deborah Kitchin

def main() -> None:  # Include in all programs. Defines the function main. We will learn more about this later.
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
    print(
        f"Hello, {firstName} {lastName}. You are {age}. You are a {profession}. You were a member of {affiliation}.\n")

    # Calculated values
    print(f"{firstName} is {age - myAge} older than {myName}")


# This decision (if statement) checks to see if the program is being run from this
# program or referenced from another program. We will learn more about this later.
if __name__ == "__main__":  # Include in all programs. Checks to see if running from this program.
    main()  # Include in  all programs. Calls main
