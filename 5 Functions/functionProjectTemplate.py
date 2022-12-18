#@copyright Deborah
def main():
    name=getName()
    address=getAddress()
    playerName=getPlayerName()
    privacy=getPrivacy()
    print("Name:", name)
    print("Address:", address)
    print("Player Name:",playerName)
    print("Privacy:",privacy)
    
def getName():
    first=""
    middle=""
    last=""
    ''' First name is done for you. You can use this technique for many other 
    parts of this assignment... street, city...'''
    while len(first) == 0:
        first=input("Enter first name ")
    # FIXME: rest of name logic goes in here and invalid setting may need to be moved.
            
    return first+" "+middle+" "+last

def getAddress():
    street="FIXME"
    city="FIXME"
    state="FIXME"
    zipCode="FIXME"
    # FIXME: address logic here
    return street+", "+city+", "+state+" "+zipCode

def getPlayerName():
    return "FIXME: Need to put player name logic in this function"

def getPrivacy():
    return "FIXME: Need to put privacy logic in this function"

main()