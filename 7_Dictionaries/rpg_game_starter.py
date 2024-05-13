
#*********** Global Variables **********
inventory = [] #an inventory, which is initially empty
currentRoom = 1 #start the player in room 1
#a dictionary linking a room to other room positions
rooms = {

            1 : {  "name"  : "Hall" ,
                   "east"  : 2,
                   "south" : 3}  ,

            2 : {  "name"  : "Bedroom" ,
                   "west"  : 1,
                   "south" : 4,
                   "item"  : "sword" }  ,            

            3 : {  "name"  : "Kitchen" ,
                   "north" : 1 }  ,

            4 : {  "name"  : "Bathroom" ,
                   "north" : 2 } 

         }

def main()->None:
    
    showInstructions()
    
    global currentRoom
    global inventory
    
    # Game loop - loop infinitely 
    while True:
    
        showStatus()
    
        '''
        Get the player's next 'move'. 
        .split() breaks it up into an list array.
        Typing 'go east' would give the list:
        ['go','east'] '''

        move = []
        while len(move) == 0:
            move = input(">").lower().split()

        #if they type 'go' first
        if move[0] == "go":
            goToRoom(move)
        
        #if they type 'get' first
        if move[0] == "get" :
            processInventory(move)
            
        #if they type 'menu' first
        if move[0] == "menu" :
            showInstructions()

def showInstructions()->None:
    
    # comment
    print("RPG Game")
    print("========")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")
    print("'menu'")

def showStatus()->None:
    
    global currentRoom
    global inventory

    #print the player's current status
    print("---------------------------")

    print(f'You are in the "{rooms[currentRoom]["name"]}"')
    
    #print the current inventory
    print(f'Inventory : {str(inventory)}')
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print(f'You see a {rooms[currentRoom]["item"]}')

    print("---------------------------")
    
def goToRoom(move)->None:
    
    global currentRoom

    # check that a direction is specified
    if len(move) == 1:
        print(f"Please indicate a direction")
    #check that they are allowed wherever they want to go
    elif move[1] in rooms[currentRoom]:
        #set the current room to the new room
        currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print("You can't go that way!") 
        
def processInventory(move)->None:

    global currentRoom
    global inventory
    
    # check that an item is specified
    if len(move) == 1:
        print(f"Please indicate a direction")
    #if the room contains an item, and the item is the one they want to get
    elif "item" in rooms[currentRoom] and move[1] == rooms[currentRoom]["item"]:
        #add the item to their inventory
        inventory += [move[1]]
        #display a helpful message
        print(f"{move[1]} got!")
        #delete the item from the room
        del rooms[currentRoom]["item"]
    #otherwise, if the item isn't there to get
    else:
        #tell them they can't get it
        print(f"Can't get {move[1]}!")    

if __name__ == "__main__":
    main()
