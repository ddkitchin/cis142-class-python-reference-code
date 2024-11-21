class Vehicle:
    
    def __init__(self,numberOfTires:int)->None:
        self._numberOfTires = numberOfTires
        
    def getNumberOfTires(self)->int:
        return self._numberOfTires
        
    def setNumberOfTires(self,numberOfTires:int):
        self._numberOfTires = numberOfTires
        
    def getDescription(self)->str:
        return f'\tThe class is {self.__class__.__name__}\n\tA vehicle with {self.getNumberOfTires()} tires.'
    
class Car(Vehicle):
    
    def __init__(self)->None:
        self._plateNumber = "**None**"
        super().__init__(4)
        
    def setLicensePlateNumber(self,plateNumber:str)->None:
        self._plateNumber = plateNumber
        
    def getDescription(self)->str:
        return f'{super().getDescription()}\n\tA vehicle with {self._plateNumber} plate.'