#@copyright Deborah Kitchin
def main():

    # Note: I am using a variable name nameKey. This is not very "pythonic".
    # In python you don't want to name variables with an indication of the type.
    # Python is a typeless language.

    # Create a dictionary
    words={"hello": "bonjour", "goodbye": "adieu","bathroom": "toilet", \
           "please": "s'il vous plait", "thank You": "merci"}

    # Get the value of a key in the dictionary
    print(words)
    wordKey="hello"
    print(f'{wordKey.capitalize()} translates to {words[wordKey]}')

    # Add a new item to the dictionary
    print("="*25)
    wordKey="yes"
    word=input(f"Enter the french word for {wordKey} ")
    words[wordKey]=word

    # Go through all the items in the dictionary
    print("="*25)
    for wordKey in words:
        print(f'{wordKey:<15}translates to\t\t{words[wordKey]}')

    # Delete an item in the dictionary with a pop.
    print("="*25)
    wordKey=input("Enter the english word to delete ")
    answer = words.pop(wordKey)
    print(f'The key {wordKey} with the value {answer} was deleted')
    for wordKey in words:
        print(f'{wordKey} translates to {words[wordKey]}')

    # Delete an item in the dictionary with a del.
    print("="*25)
    wordKey=input("Enter the english word to delete ")
    del words[wordKey]
    for wordKey in words:
        print(f'{wordKey} translates to {words[wordKey]}')

    # Check if a key is in the dictionary
    print("=" * 25)
    wordKey = "starter"
    while wordKey != "":
        if wordKey in words:
            print(f'{wordKey} translates to {words[wordKey]}')
        else:
            print(f'{wordKey} is not in the dictionary')
        wordKey = input(f'Enter a word to look up ')

    # Morse code dictionary.
    morseCode={"A": ".-",       "N": "-.",      "0": "-----", \
               "B": "-...",     "O": "---",     "1": ".----", \
               "C": "-.-.",     "P": ".--.",    "2": "..---", \
               "D": "-..",      "Q": "--.-",    "3": "...--", \
               "E": ".",        "R": ".-.",     "4": "....-", \
               "F": "..-.",     "S": "...",     "5": ".....", \
               "G": "--.",      "T": "-",       "6": "-....", \
               "H": "....",     "U": "..-",     "7": "--...", \
               "I": "..",       "V": "...-",    "8": "---..", \
               "J": ".---",     "W": ".--",     "9": "----.", \
               "K": "-.-",      "X": "-..-",    ".": ".-.-.-", \
               "L": ".-..",     "Y":"-.--",     ",": "--..--", \
               "M": "--",       "Z": "--..",    "?": "..--.."}

    print(morseCode)

    from operator import itemgetter
    print(sorted(morseCode.items(), key=itemgetter(0)))

    name="Debbie"
    print(morseCode["D"])
    while name !="":
        print(f'{name} is ',end="")
        for char in name.upper():
            print(morseCode[char]," ",end="")
        print()
        name=input("Enter another word ")

if __name__ == "__main__":
    main()