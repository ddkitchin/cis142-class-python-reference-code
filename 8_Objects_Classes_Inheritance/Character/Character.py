# @copyright Deborah Kitchin

class Character:

    def __init__(self, name:str, strength:int, health:int)->None:
        self._name = name
        # set _strength, _health, and _magic

    def getName(self)->str:
        # return _name
        return ""

    def getStrength(self)->int:
        # return _strength
        return ""

    def getHealth(self)->int:
        # return _health
        return ""

    def getMagic(self)->int:
        # return _magic
        return ""

    def adjustHealth(self, health:int)->None:
        # change _health based on the health passed in
        # remove this line. it is here to avoid syntax errors
        3 + 2
