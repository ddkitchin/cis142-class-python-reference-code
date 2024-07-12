##
#  This program counts the number of unique words.txt contained in a text document,
#  using a list.
#
def main() -> None:
    uniqueWords = []

    filename = input("Enter filename (default: nursery_rhyme.txt): ")
    if len(filename) == 0:
        filename = "nursery_rhyme.txt"
    inputFile = open(filename, "r")

    for line in inputFile:
        theWords = line.split()
        for word in theWords:
            cleaned = clean(word)
            if cleaned != "" and cleaned not in uniqueWords:
                uniqueWords.append(cleaned)

    print("The document contains", len(uniqueWords), "unique words.txt.")


## Cleans a string by making letters lowercase and removing characters 
#  that are not letters.
#  @param string the string to be cleaned
#  @return the cleaned string
#
def clean(string: str) -> str:
    result = ""
    for char in string:
        if char.isalpha():
            result = result + char.lower()

    return result


# Start the program.
if __name__ == "__main__":
    main()
