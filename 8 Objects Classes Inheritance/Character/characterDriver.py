#@copyright Deborah Kitchin

from character import Character

def main():

    print("TEAM 1")
    # create team 1 using createCharacter() to create each character.
    # team1 is a string to avoid syntax errors. Change it to a list, set or
    # dictionary holding the 3 Character objects created from the Character class.
    team1=""

    print("TEAM 2")
    # create team 2 using createCharacter() to create each character
    # team2 is a string to avoid syntax errors. Change it to a list, set or
    # dictionary holding the 3 Character objects created from the Character class.
    team2=""
    
    for i in range(3): 
        fight(team1,team2)
        
    printFinalResults(team1,team2)
        
'''createCharacter creates an object of class Character and returns that object.
As written, ther are no parameters to createCharacter. Inside this function you 
will set the name, strength and health to something other than 0 in any manner
you choose (input, random number...) 

You can adjust createCharacter to pass name, strength and health as parameters
and then the function return the object of type class.

You do not have to use createCharacter if you want to create your objects in your own way.'''
def createCharacter():
    name=""
    #make sure the name is not empty
        
    strength=0
    #set rule for strength and make sure the character follows your rule
            
    health=0
    #set rule for health and make sure the character follows your rule

    # the return below creates the charcter object from the Character class with
    # the values you set for name, strength, and health
    return Character(name,strength,health)

def fight(team1,team2):
    totalStrength1=0
    # calculate team 1s strength and save it to compare to team1
    
    totalStrength2=0
    # calculate team2s strength and save it to compare to team1
        
    if totalStrength1 > totalStrength2:
        print("================Team 1 won====================")
        #adjust team1 and team2's charcter's health based on the result
    elif totalStrength2 > totalStrength1:
        print("================Team 2 won====================")
        #adjust team1 and team2's charcter's health based on the result
    else:
        print("================A Tie!!====================")
    
    printTeam(team1)
    print()
    printTeam(team2)

def printTeam(team):
    print("Name        Strength      Health        Magic")
    # print the team members names, strength, health, and magic

def printFinalResults(team1,team2):
    print("****************** Final Results **********************")
    # print the final results
        
main()