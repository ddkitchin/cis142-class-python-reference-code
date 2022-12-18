#@copyright Deborah Kitchin
def main():
    privacy = getPrivacy()
    print(privacy)
    
#@ return Public or Private based on players preference
def getPrivacy():
    privacy=""
    while privacy  != "Y" and privacy != "N":
        privacy=input("Do you want your profile protected from others? y or n ").upper()
    if privacy.upper() == "Y":
        return "Private"
    else:
        return "Public"
    
main()