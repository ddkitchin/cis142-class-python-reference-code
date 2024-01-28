from datetime import date

def main():

    NAME = "Penny" #string
    BREED = "Golden Lab" #string
    AGE = 5 # integer
    DOG_YEARS_TO_HUMAN_YEARS = 7 # integer
    AVERAGE_DOG_LIFE = 15 # integer

    humanAge = AGE * DOG_YEARS_TO_HUMAN_YEARS # integer * integer = integer
    dogLifeComplete = AGE / AVERAGE_DOG_LIFE # integer / integer = real number.

    # This is the way you should print according to class style guidelines.
    # f-string formatting
    print(f'My pet {NAME} is a {BREED}. She is {AGE} years old.\nIn human years she is {humanAge} and has completed about {dogLifeComplete:.2f} of their life.')

    # This is the way we did it in class before Python 3.6
    print() # blank line
    print('My pet %s is a %s. She is %d years old.\nIn human years she is %d and has completed about %.2f of their life.' % (NAME, BREED, AGE, humanAge, dogLifeComplete))

    # fields with no text between values
    # Using rount and 2 digit percision.

    print() # blank line
    print(NAME, BREED, AGE, humanAge, round(dogLifeComplete, 2))

if __name__ == '__main__':
    main()
