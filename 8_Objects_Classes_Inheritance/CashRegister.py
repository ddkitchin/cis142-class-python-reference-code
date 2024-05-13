class CashRegister :
 
      #def __init__(self): # Line to add when tax is not required
      def __init__(self, taxRate:float=0.0)->None: # Line to use when tax is required
            self._itemCount = 0
            self._totalPrice = 0.0
            self._taxableTotal = 0.0 # Line to add when tax is required
            self._taxRate = taxRate # Line to add when tax is required

      #def addItem(self, price): # Line to add when tax is not required
      def addItem(self, price:float, taxable:bool=False)->None: # Line to use when tax is required
            self._itemCount = self._itemCount + 1
            self._totalPrice = self._totalPrice + price
            if taxable: # Line to add when tax in required
                  self._taxableTotal += price # Line to add when tax is required
      
      def getTotal(self)->str:
            #return self._totalPrice # Line to add when tax is not required
            return self._totalPrice + self._taxableTotal * self._taxRate / 100 # Line to add when tax is required
            
      def getCount(self)->int:
            return self._itemCount

      def clear(self)->None:
            #must pass tax rate to init, otherwise set to 0.
            self.__init__(self._taxRate)
