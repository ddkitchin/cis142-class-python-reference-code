#@copyright Deborah Kitchin

birthMonth=int(input("Enter your month "))
checkDate1=0
checkDate2=0

'''If the month is January, February, or March, you make less checks with Algorithm 1
than if you use Algorithm 2. For all other months you make less checks with 
Algorithm 2. 

Algoritm 1 has right drift. Algorithm 3 shows same algorithm as Algorithm 1,
but with python elif keyword insead of the puthon else if. Algorithm 3 
can not count the decisions because the else and if are combined into the elif.'''

print("Algorithm 1 ",end="")
checkDate1+=1
if birthMonth == 1:
    print("January ",checkDate1," check")
else:
    checkDate1+=1
    if birthMonth == 2:
        print("February ",checkDate1," checks")
    else:
        checkDate1+=1    
        if birthMonth == 3:
            print("March ",checkDate1," checks")
        else:
            checkDate1+=1    
            if birthMonth == 4:
                print("April ",checkDate1," checks")
            else:
                checkDate1+=1    
                if birthMonth == 5:
                    print("May ",checkDate1," checks")
                else:
                    checkDate1+=1
                    if birthMonth == 6:
                        print("June ",checkDate1," checks")
                    else:
                        checkDate1+=1
                        if birthMonth == 7:
                            print("July ",checkDate1," checks")
                        else:
                            checkDate1+=1
                            if birthMonth == 8:
                                print("August ",checkDate1," checks")
                            else:
                                checkDate1+=1
                                if birthMonth == 9:
                                    print("September ",checkDate1," checks")
                                else:
                                    checkDate1+=1
                                    if birthMonth == 10:
                                        print("October ",checkDate1," checks")
                                    else:
                                        checkDate1+=1
                                        if birthMonth == 11:
                                            print("November ",checkDate1," checks")
                                        else:
                                            print("December ",checkDate1," checks")

print("Algorithm 2 ",end="")
checkDate2+=1
if birthMonth < 7:
    checkDate2+=1
    if birthMonth < 4:
        checkDate2+=1
        if birthMonth < 2:
            print("January ",checkDate2," checks")
        else:
            checkDate2+=1
            if birthMonth < 3:
                print("February ",checkDate2," checks")
            else:
                print("March ",checkDate2," checks")
    else:
        checkDate2+=1
        if birthMonth < 5:
            print("April ",checkDate2," checks")
        else:
            checkDate2+=1
            if birthMonth < 6:
                print("May ",checkDate2," checks")
            else:
                print("June ",checkDate2," checks")
else:
    checkDate2+=1
    if birthMonth < 10:
        checkDate2+=1
        if birthMonth < 8:
            print("July ",checkDate2," checks")
        else:
            checkDate2+=1
            if birthMonth < 9:
                print("August ",checkDate2," checks")
            else:
                print("September ",checkDate2," checks")
    else:
        checkDate2+=1
        if birthMonth < 11:
            print("October ",checkDate2," checks")
        else:
            checkDate2+=1
            if birthMonth < 12:
                print("November ",checkDate2," checks")
            else:
                print("December ",checkDate2," checks")
                
''' Algorithm 1 and 3 ARE THE SAME ALGORITHM. You are using different python
syntax (Algorithm 1 is if...else...if....else 
versus Algorithm 2 is if...elif...elif...elif...)
so they look different but they are the same algorithm.'''

print("Algorithm 3 ",end="")

if birthMonth == 1:
    print("January ")
elif birthMonth == 2:
    print("February ")
elif birthMonth == 3:
    print("March ")
elif birthMonth == 4:
    print("April ")
elif birthMonth == 5:
    print("May ")
elif birthMonth == 6:
    print("June ")
elif birthMonth == 7:
    print("July ")
elif birthMonth == 8:
    print("August ")
elif birthMonth == 9:
    print("September ")
elif birthMonth == 10:
    print("October ")
elif birthMonth == 11:
    print("November ")
else:
    print("December ")