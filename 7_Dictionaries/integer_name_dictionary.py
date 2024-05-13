#  This program turns an integer into its English name using a dictionary.
def main()-> None:
    keepGoing = True
    while keepGoing:
        value = int(input("Please enter a positive integer < 1000: "))
        if 0 < value < 1000:
            print(intName(value))
        else:
            print("Please enter a number between 1 and 999.")
        keepGoing = input("Do you want to keep going Y/N ")[0].upper() == "Y"


#  @return the name of the number (e.g. "two hundred seventy four")
def intName(number:int)->str:

    # The number that still needs to be converted.
    name = ""  # Start name with empty string.

    # If the number is > 100
    if number >= 100:
        # pass the 100s digit to digit name to get the word.
        name = digitName[number // 100] + " hundred"
        # remove the 100s digit from number
        number = number % 100

    # if 10s digit is 20 or higher, use the tensName converter and remove the 10s digit
    if number >= 20:
        name = name + " " + tensName[number // 10]
        number = number % 10
    # if 10s digit is a teen, use the teens converter and you are done.
    elif number >= 10:
        name = name + " " + teenName[number]
        number = 0

    # do the 1s digit using digitName
    if number > 0:
        name = name + " " + digitName[number]

    return name

#  @return the digit name
digitName = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

#  @return the teens name
teenName = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

#  @return tens word
tensName = {
    9: "ninety",
    8: "eighty",
    7: "seventy",
    6: "sixty",
    5: "fifty",
    4: "forty",
    3: "thirty",
    2: "twenty"
}

if __name__ == "__main__":
    main()