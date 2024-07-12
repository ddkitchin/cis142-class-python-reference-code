# @copyright Deborah Kitchin
def main() -> None:
    name = getName()
    address = getAddress()
    playerName = getPlayerName()
    privacy = getPrivacy()
    print(name)
    print(address)
    print(playerName)
    print(privacy)


def validFirstName(first: str) -> bool:
    # @return True if first name is not empty

    if len(first) == 0:
        print("ERROR: A first name is required")
        return False
    else:
        return True


def validMiddleName(middle: str) -> str:
    # @return middle name and a space unless middle name is empty.

    return "FIX ME"


def validLastName(first: str, last: str) -> str:
    # @return True is last name is valid otherwise false

    return "FIX ME"


def getName() -> str:
    # @return First Middle and Last Name Validated.
    # There should be a space after the first name.

    ''' First name is done for you. You can use this technique for many other
    parts of this assignment... street, city...'''
    first = input("Enter first name ")
    while not validFirstName(first):  # Notice the call to validFirstName
        first = input("Enter first name ")

    middle = "FIX ME"  # use validMiddleName(middle)

    last = "FIX ME"  # use validLastName (first,Last) similar to how first name is done above.

    return first + " " + middle + last


def validStreet(street: str) -> str:
    # @return True if street is not empty

    return "FIX ME"


def validCity(city: str) -> str:
    # @return True if city is not empty

    return "FIX ME"


def validState(state: str) -> str:
    # @return True if state is not empty

    return "FIX ME"


def validZipCode(zipCode: str) -> str:
    # @return True if zipcode is valid

    return "FIX ME"


def getAddress() -> str:
    # @return valid "street, city state zipcode"

    street = "FIX ME"  # use validStreet (street) similar to how first name is done above.

    city = "FIX ME"  # use validCity (city) similar to how first name is done above

    state = "FIX ME"  # use validState (state) similar to how first name is done above

    zipCode = "FIX ME"  # use validZipCode (zipCode) similar to how first name is done above

    return street + ", " + city + ", " + state + " " + zipCode


def validPlayerName(playerName: str) -> bool:
    # @return True if valid player name.

    return "FIX ME"


def confirmPlayerName(playerName: str, playerName2: str) -> bool:
    # @return True if player names match, otherwise False

    return "FIX ME"


def getPlayerName() -> str:
    # @return valid player name

    playerName = "FIX ME"  # use validPlayerName (playerName) similar to how first name is done above

    playerName2 = "FIX ME"  # use confirmPlayerName (playerName, playerName2) similar to how first name is done above

    return "FIX ME"


def validPrivacy(privacy: str) -> bool:
    # @return True if Y or N were selected otherwise False

    return "FIX ME"


def getPrivacy() -> str:
    # @return validated Public or Private visibility.

    return "FIX ME"  # use validPrivacy (privacy) similar to how first name is done above


if __name__ == "__main__":
    main()
