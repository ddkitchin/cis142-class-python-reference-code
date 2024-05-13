# Models a tally counter whose value can be incremented, viewed, or reset.

class Counter :   
   
   ''' When dunder init (__init__) is not specified none of the attributes are set.
   In this example, you would have to call the reset to get the value set to 0
   def __init__(self)->None:
      self._value = 0'''
    
   def getValue(self) ->int:
      return self._value

   def click(self) ->None:
      self._value = self._value + 1

   def reset(self)->None :
      self._value = 0
      #self.__init__() # Or you can just call the dunder init __init__()
