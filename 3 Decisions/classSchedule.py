totalHours = 0

classHours=int(input("Enter class hours "))

while totalHours +  classHours <= 16:
    totalHours = totalHours + classHours
    #print(f'In Loop totalHours = {totalHours}')    
    classHours=int(input("Enter class hours "))  
    
print(f'totalHours = {totalHours}')