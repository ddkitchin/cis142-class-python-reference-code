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
if NAME == c.getName():
    print(c.getName(),R)
else:
    print(c.getName(),W)
    
# check strength
if STRENGTH == c.getStrength():
    print(c.getStrength(),R)
else:
    print(c.getStrength(),W)
    
# check health
if HEALTH == c.getHealth():
    print(c.getHealth(),R)
else:
    print(c.getHealth(),W)
    
# adjust health and show new health
c.adjustHealth(1)
print("Health after adjustment of 1",c.getHealth())

# show magic
print("Magic is set by game designer within the constructor",c.getMagic())

