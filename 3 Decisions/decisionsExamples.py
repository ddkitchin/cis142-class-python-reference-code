#@copyright Deborah Kitchin

# variable haveDog set to user input. Notice = this is the algebraic equal sign
haveDog=input("Do you have a dog? (Y or N): ")

# notice this is a ==. This is the boolean equal.
# One-way if
if haveDog.upper() == "Y":
    print ("Arf, Arf")
    
# notice this is a ==. This is the boolean equal. This would allow someone to
# enter "Yes" or "yes" and still get the bark.
# One-way if
if haveDog.upper()[0] == "Y":
    print ("Arf, Arf") 

######################################################################
   
# Two-way if
isLightOn=input("Is the light on? (Y or N) ")
if isLightOn.upper()=="Y":
    print("Please turn the light off before you leave")
else:
    print("Have a nice day")

######################################################################
# Earthquake program. Both are the same algorithm just using else/if or elif.
# Both are multi-way decisions

# Obtain magnitude
richter = float(input("Enter a magnitude on the Richter scale: "))
    
# Print the description
if richter >= 8.0:
    print("Most structures fall")
elif richter >= 7.0:
    print("Many buildings destroyed")
elif richter >= 6.0:
    print("Many buildings considerably damaged, some collapse")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings")
else: 
    print("No destruction of buildings")

if richter >= 8.0:
    print("Most structures fall")
else:
    if richter >= 7.0:
        print("Many buildings destroyed")
    else:
        if richter >= 6.0:
            print("Many buildings considerably damaged, some collapse")
        else:
            if richter >= 4.5:
                print("Damage to poorly constructed buildings")
            else: 
                print("No destruction of buildings")

######################################################################
# 2 Algorithms to determine a grade based on the score.
    
# Algorithm 1 - Check from the bottom up (F to A)
# Multi-way if determing the letter grade for a test score
MIN_D=60
MIN_C=70
MIN_B=80
MIN_A=90
testScore=int(input("Please enter a score between 0 and 100 "))
if testScore < MIN_D:
    print("F")
elif testScore < MIN_C:
    print("D")
elif testScore < MIN_B:
    print("C")
elif testScore < MIN_A:
    print("B")
else:
    print("A")
    
# Algorithm 2 - Check in the middle than narrow in on decision.
# Nested, two-way and multi-way if determing the letter grade for a test score. 
# Same result as previous.
if testScore < MIN_C:
    if testScore < MIN_D:
        print("F")
    else:
        print("D")
elif testScore < MIN_A:
    if testScore < MIN_B:
        print("C")
    else:
        print("B")
else:
    print("A")

# This is the really the same algorithm as Algorithm 1. 
# Notice this algorithm does not takeadvantage
# of previous if checks and rechecks information it already knows.
if testScore >= 0 and testScore < MIN_D:
    print("F")
elif testScore >= MIN_D and testScore < MIN_C:      # you can only get here if testScore >= MID_D
    print("D")
elif testScore >= MIN_C and testScore < MIN_B:      # you can only get here if testScore >= MIN_C
    print("C")
elif testScore >= MIN_B and testScore < MIN_A:      # you can only get here if testScore >= MIN_B 
#elif testScore >= MIN_B and testScore <= MIN_A:    # this is the same as line above
    print("B")
elif 100 >= testScore >= MIN_A:                     # This check is unnecessary. You only get to the else if testScore >= MIN_A
    print("A")

######################################################################
   
# Demorgan's Law
stop=input("Go again (y or n) ")
# not(expr1 or expr2) look at next if same results converted using DeMorgan's Law
if not (stop == "y" or stop =="Y"):
    print("Stop")
else:
    print("Keep Going")
    
# not(expr1) and not(expr2) look above if same results converted using DeMorgan's Law
if not (stop == "y") and not (stop =="Y"):
    print("Stop")
else:
    print("Keep Going")

# --------------------------------------------------------------

# Charge more shipping for Hawaii and Alaska
state=input("Enter the state ")
# not (expr1 and expr2) same result as if below but Demorgan law conversion applied
if not (state != "Hawaii" and state != "Alaska"):
    print("Charge more shipping")
else:
    print("Regular Shipping")
        
# not (expr1) or not (expr2) same result as if above but Demorgan law conversion applied
if not (state != "Hawaii") or not (state != "Alaska"):
    print("Charge more shipping")
else:
    print("Regular Shipping")
      
######################################################################
''' in you boolean statements, if you find yourself testing for == True or 
== False, you are typing too much.  If true let the boolean speak for itself.
If false add a not to the front of the boolean.'''       

done = True
if (done == True):                              # don't do this
    print("done is true - if don't do this")
if (done):                                      # do this
    print("done is true - if do this")
    
done = False
if (done == False):                              # don't do this
    print("done is false - if don't do this")
if not (done):                                   # do this
    print("done is false - if do this")