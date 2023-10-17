# @copyright Deborah Kitchin
#
class Weapon:
    
    def __init__(self,damage):
        self._damage = damage
        
    def __repr__(self):
        # user repr to create an object from it.
        return f'{self.__class__.__name__}({self._damage})'
    
def main():
    w=Weapon(5)
    print(w)
    w2=eval(repr(Weapon(10)))
    print(w2)

if __name__ == "__main__":
    main()