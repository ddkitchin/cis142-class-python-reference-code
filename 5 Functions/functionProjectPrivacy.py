#@copyright Deborah Kitchin
def main():
    privacy = getPrivacy()
    print(privacy)
    
#@ return Public or Private based on players preference
def getPrivacy():
    
    privacy = ""
    while (len(privacy) == 0) or (privacy[0].upper() != "Y" and privacy[0].upper() != "N"):
        privacy = input("Do you want your profile private from other players (Y or N)? ")
        
    if privacy[0].upper() == "Y":
        return "Private"
    else:
        return "Public"
    
main()
