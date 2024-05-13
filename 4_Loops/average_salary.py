# @ copyright Deborah Kitchin
''' Algorithm

set total and count to 0
ask for salary
process salaries until salary 0.0 or less is entered.
    add salary to total
    add 1 to count
    ask for salary

print average salary
'''
def main()-> None:
    total = 0.0
    count = 0

    salary = float(input("Enter a salary: "))

    while salary > 0.0:
        #print(salary)
        total = total + salary
        count = count + 1
        #print(total, count)
        salary = float(input("Enter a salary: "))

    if count == 0:
        print("The average salary is 0")
    else:
        print(f'The average salary is {total/count:.2f}')

if __name__ == "__main__":
    main()