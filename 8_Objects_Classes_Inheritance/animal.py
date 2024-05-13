# @copyright Deborah Kitchin
class Animal:

    def __init__(self, sound:str="Unknown", food:str="Unknown", movement:str="run")->None:
        self._sound = sound
        self._food = food
        self._movement = movement

    def __repr__(self)->str:
        return f'Animal [{self.__class__.__name__},{self._sound},{self._food},{self._movement}]'

    def speak(self)->None:
        print(self._sound, end=" ")

    def eat(self)->None:
        print(self._food, end=" ")

    def move(self)->None:
        print(self._movement, end=" ")


class Dog(Animal):

    def __init__(self)->None:
        super().__init__("ruff", "dog food")

    def goOnWalk(self)->None:
        print("walk, walk, walk")


class Wolf(Animal):

    def __init__(self)->None:
        super().__init__("grrr", "squirrels")

    def hunt(self)->None:
        print("grrr, run, catch, kill")


class Eagle(Animal):

    def __init__(self)->None:
        super().__init__("squeal", "rabbits", "fly")

    def hunt(self)->None:
        print("squeal, fly, claw, carry, kill")


def showMe(animal:Animal)->None:
    print(animal, end=": ")
    print()
    print("\tcalling speak=", end="")
    animal.speak()
    print()
    print("\tcalling eat=", end="")
    animal.eat()
    print()
    print("\tcalling move=", end="")
    animal.move()
    # animal.goOnWalk() # wrong only dogs go on walks


def main()->None:
    print("*****Init")
    object1 = Animal()  # take defaults
    object2 = Animal('meow', 'mouse', 'prowl')  # specify attributes
    object3 = Dog()
    object4 = Wolf()
    object5 = Eagle()

    print()
    print("*****repr")
    print(object1)
    print(object2)
    print(object3)
    print(object4)
    print(object5)

    print()
    print("*****speak")
    object1.speak()
    print()
    object2.speak()
    print()
    object3.speak()
    print()
    object4.speak()
    print()
    object5.speak()
    print()

    print()
    print("*****eat")
    object1.eat()
    print()
    object2.eat()
    print()
    object3.eat()
    print()
    object4.eat()
    print()
    object5.eat()
    print()

    print()
    print("*****move")
    object1.move()
    print()
    object2.move()
    print()
    object3.move()
    print()
    object4.move()
    print()
    object5.move()
    print()

    print()
    print("***** specific function")
    object3.goOnWalk()
    # object3.hunt() #wrong dogs don't hunt
    object4.hunt()
    object5.hunt()

    print()
    print("***** calling function showMe - polymorphism")
    zoo = [object1, object2, object3, object4, object5]
    for animal in zoo:
        showMe(animal)
        print()

if __name__ == "__main__":
    main()
