#@copyright Deborah Kitchin
def main():
    words={"hello": "bonjour", "goodbye": "adieu","bathroom": "toilet", \
           "Please": "S'il vous plait", "Thank You": "Merci"}

    print(words)
    print(f'Hello translates to {words["hello"]}')

    print("="*25)
    word=input("Enter the french word for yes ")
    words["yes"]=word

    for word in words:
        print(f'{word} translates to {words[word]}')

    print("="*25)
    word=input("Enter the english word to delete ")
    words.pop(word)
    print("="*25)
    for word in words:
        print(f'{word} translates to {words[word]}')

    morseCode={"A": ".-", "N": "-.", "0": "-----", \
               "B": "-...", "O": "---", "1": ".----", \
               "C": "-.-.", "P": ".--.", "2": "..---", \
               "D": "-..", "Q": "--.-", "3": "...--", \
               "E": ".","R": ".-.", "4": "....-", \
               "F": "..-.", "S": "...", "5": ".....", \
               "G": "--.", "T": "-", "6": "-....", \
               "H": "....", "U": "..-", "7": "--...", \
               "I": "..", "V": "...-", "8": "---..", \
               "J": ".---", "W": ".--", "9": "----.", \
               "K": "-.-", "X": "-..-", ".": ".-.-.-", \
               "L": ".-..", "Y":"-.--", ",": "--..--", \
               "M": "--", "Z": "--..", "?": "..--.."}

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