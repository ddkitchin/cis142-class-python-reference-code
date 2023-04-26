#@copyright Deborah Kitchin
class Treasure :
    
    def __init__(self, name="", value=0):
        self._name = name
        self._value = value
        
    def getName(self):
        return self._name
                
    def setName(self, name):
        self._name = name

    def getValue(self):
        return self._value
    
    def setValue(self, value):
        self._value = value
    
    def __str__(self):
        return f'Treasure Item {self._name} is worth {self._value}'
    
    def __repr__(self):
        return self.__str__()
    
def main():
    playerTreasureChest = []
    
    # add prizes to treasure chest
    while input("Do you want to continue ").upper() != "N":
        name = input("Enter the prize name ")
        value = int(input("Enter the prize value "))
        playerTreasureChest.append(Treasure(name,value))
        
    print(playerTreasureChest) # not meaningful unless you implement __repr__
    for prize in playerTreasureChest:
        print(prize)
        
    # print out the prizes
    totalValue = 0
    for prize in playerTreasureChest:
        print(f'{prize.getName()} is worth {prize.getValue()}')
        totalValue += prize.getValue() 
    print(f'Total value is {totalValue}.')
            
    # change prize values
    for prize in playerTreasureChest:
        prize.setValue(10 * prize.getValue())
        
    # print out the prizes again
    totalValue = 0
    for prize in playerTreasureChest:
        print(f'{prize.getName()} is worth {prize.getValue()}')
        totalValue += prize.getValue()  

    print(f'Total value is {totalValue}.')    

main()
    
