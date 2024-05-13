# @copyright Deborah Kitchin

def main()-> None:

    totalHours = 0

    classHours=int(input("Enter class hours "))

    while totalHours +  classHours <= 16:
        totalHours = totalHours + classHours
        #print(f'In Loop totalHours = {totalHours}')
        classHours=int(input("Enter class hours "))

    print(f'totalHours = {totalHours}')

if __name__ == "__main__":
    main()