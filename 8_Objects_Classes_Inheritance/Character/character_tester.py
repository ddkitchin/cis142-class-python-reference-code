#Character tester
#@copyright Deborah Kitchin

from Character import Character

def main() -> None:
    #Constants
    NAME = "Master Chief"
    STRENGTH = 10
    HEALTH = 20
    R = "RIGHT"
    W = "WRONG"

    # create a character
    c = Character(NAME, STRENGTH, HEALTH)

    # check name
    print(f'getName() test is ', end="")
    if NAME == c.getName():
        print(f'{c.getName()} {R}')
    else:
        print(f'{c.getName()} {W}')
    print()

    # check strength
    print(f'getStrength() test is ', end="")
    if STRENGTH == c.getStrength():
        print(f'{c.getStrength()} {R}')
    else:
        print(f'{c.getStrength()} {W}')
    print()

    # check health
    print(f'getHealth() test is ', end="")
    if HEALTH == c.getHealth():
        print(f'{c.getHealth()} {R}')
    else:
        print(f'{c.getHealth()} {W}')
    print()

    # adjust health and show new health
    c.adjustHealth(1)
    print(f'getHealth() after adjustment of 1 {c.getHealth()}. Verify this is what you programmed.')
    print()
    # show magic
    print(f'getMagic() is set by game designer within the constructor {c.getMagic()}. Verify it is set the way you programmed.')
    print()

    # Verify class attributes have correct name with _ before the name.
    assert c._name == c.getName(), f'c._name not found. Name attribute must be named _name'
    assert c._strength == c.getStrength(), f'c._stength not found. Name attribute must be named _strength'
    assert c._health == c.getHealth(), f'c._health not found. Name attribute must be named _health'
    assert c._magic == c.getMagic(), f'c._magic not found. Name attribute must be named _magic'

if __name__ == "__main__":
    main()