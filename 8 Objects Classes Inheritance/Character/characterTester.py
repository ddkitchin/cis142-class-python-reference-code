#Character tester
#@copyright Deborah Kitchin

from character import Character

#Constants
NAME="Master Chief"
STRENGTH=10
HEALTH=20
R="RIGHT"
W="WRONG"

# create a character
c=Character(NAME,STRENGTH,HEALTH)

# check name
print(f'getName() test is ',end="")
if NAME == c.getName():
    print(f'{c.getName()} {R}')
else:
    print(f'{c.getName()} {W}')
    
# check strength
print(f'getStrength() test is ',end="")
if STRENGTH == c.getStrength():
    print(f'{c.getStrength()} {R}')
else:
    print(f'{c.getStrength()} {W}')
    
# check health
print(f'getHealth() test is ',end="")
if HEALTH == c.getHealth():
    print(f'{c.getHealth()} {R}')
else:
    print(f'{c.getHealth()} {W}')
    
# adjust health and show new health
c.adjustHealth(1)
print(f'getHealth() after adjustment of 1 {c.getHealth()}. Verify this is what you programmed.')

# show magic
print(f'getMagic() is set by game designer within the constructor {c.getMagic()}. Verify it is set the way you programmed.')