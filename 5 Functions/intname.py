#  This program turns an integer into its English name.
def main() :
   value = int(input("Please enter a positive integer < 1000: "))
   print(intName(value))

#  @return the name of the number (e.g. "two hundred seventy four")
def intName(number) :
   
   # The number that still needs to be converted.
   name = ""   # Start name with empty string.

   # If the number is > 100
   if number >= 100 :
      # pass the 100s digit to digit name to get the word.
      name = digitName(number // 100) + " hundred"
      # remove the 100s digit from number
      number = number % 100

   # if 10s digit is 20 or higher, use the tensName converter and remove the 10s digit
   if number >= 20 :
      name = name + " " + tensName(number)
      number = number % 10
   # if 10s digit is a teen, use the teens converter and you are done.
   elif number >= 10 :
      name = name + " " + teenName(number)
      number = 0
   
   # do the 1s digit using digitName
   if number > 0 :
      name = name + " " + digitName(number)

   return name

#  @return the digit name
def digitName(number) :
   if number == 1 : return "one"
   if number == 2 : return "two"
   if number == 3 : return "three"
   if number == 4 : return "four"
   if number == 5 : return "five"
   if number == 6 : return "six"
   if number == 7 : return "seven"
   if number == 8 : return "eight"
   if number == 9 : return "nine"
   return ""

#  @return the teens name
def teenName(number) :
   if number == 10 : return "ten"
   if number == 11 : return "eleven"
   if number == 12 : return "twelve"
   if number == 13 : return "thirteen"
   if number == 14 : return "fourteen"
   if number == 15 : return "fifteen"
   if number == 16 : return "sixteen"
   if number == 17 : return "seventeen"
   if number == 18 : return "eighteen"
   if number == 19 : return "nineteen"
   return ""

#  @return tens word
def tensName(number) :
   if number >= 90 : return "ninety"
   if number >= 80 : return "eighty"
   if number >= 70 : return "seventy"
   if number >= 60 : return "sixty"
   if number >= 50 : return "fifty"
   if number >= 40 : return "forty"
   if number >= 30 : return "thirty"
   if number >= 20 : return "twenty"
   return ""

main()
