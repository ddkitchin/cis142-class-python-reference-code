#@copyright Deborah Kitchin
# @copyright Deborah Kitchin
def main():
    privacy = getPrivacy()
    print(privacy)


def validPrivacy(privacy):
    # @return True if Y or N were selected otherwise False

    if len(privacy) != 0 and (privacy[0].upper() == "Y" or privacy[0].upper() == "N"):
        return True
    else:
        print("ERROR: Privacy must be Y or N")
        return False


def getPrivacy():
    # @return validated Public or Private visibility.

    privacy = input("Do you want your profile visible to others Y or N? ")
    while not validPrivacy(privacy):
        privacy = input("Do you want your profile visible to others Y or N? ")

    if privacy[0].upper() == "N":
        return "Private"
    else:
        return "Public"


main()