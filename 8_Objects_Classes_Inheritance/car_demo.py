from Car import Car,Vehicle # or * instead of Car,Vehicle

def main()->None:
    aPlainCar=Car()
    #print(aPlainCar.getNumberOfTires()) #need to test
    #print(aPlainCar.getDescription()) #need to test
    printInfo(aPlainCar)     
    
    aPlainCar.setNumberOfTires(6)  
    #print(aPlainCar.getDescription())
    printInfo(aPlainCar) 
    
    aLimo = Car()
    aLimo.setLicensePlateNumber("WOOHOO")
    aLimo.setNumberOfTires(8)
    printInfo(aLimo)     
    
    v = Vehicle(10)
    printInfo(v)     

def printInfo(car:Car)->None: #dynamic lookup of objects of type Car or Vehicle will work.
    print("===car attibutes===")
    print(car.getDescription())
    
if __name__ == "__main__":
    main()