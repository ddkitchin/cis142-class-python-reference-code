class Vehicle:
    
    def __init__(self,numberOfTires):
        self._numberOfTires = numberOfTires
        
    def getNumberOfTires(self):
        return self._numberOfTires
        
    def setNumberOfTires(self,newValue):
        self._numberOfTires = newValue
        
    def getDescription(self):
        return f'\tThe class is {self.__class__.__name__}\n\tA vehicle with {self.getNumberOfTires()} tires.'
    
class Car(Vehicle):
    
    def __init__(self):
        self._plateNumber = "**None**"
        super().__init__(4)
        
    def setLicensePlateNumber(self,newValue):
        self._plateNumber = newValue
        
    def getDescription(self):
        return f'{super().getDescription()}\n\tA vehicle with {self._plateNumber} plate.'