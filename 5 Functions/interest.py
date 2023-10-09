# @copyright Deborah Kitchin
def main() :
   initialBalance = 10000
   rate = 4
   years = 3
   print(f'In {years} years at {rate}%, ${initialBalance:,} will be ${futureValue(initialBalance, rate, years):,.2f}.')
   
   initialBalance = 5000
   rate = 3.5
   years = 4
   print(f'In {years} years at {rate}%, ${initialBalance:,} will be ${futureValue(initialBalance, rate, years):,.2f}.')

   initialBalance = 1000
   rate = 10
   years = 1
   print(f'In {years} years at {rate}%, ${initialBalance:,} will be ${futureValue(initialBalance, rate, years):,.2f}.')

   initialBalance = int(input("Enter initial balance: "))
   rate = float(input("Enter rate: "))
   years = int(input("Enter years: "))
   print(f'In {years} years at {rate}%, ${initialBalance:,} will be ${futureValue(initialBalance, rate, years):,.2f}.')
   
#  @return the future value of the investment
def futureValue(initialBalance, rate, years) :
   return initialBalance * (1 + rate / 100) ** years

main()
