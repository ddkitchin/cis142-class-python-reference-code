##
#  This program counts the number of unique words.txt contained in a text document.
#

def main() :
   uniqueWords = set()
   
   filename = input("Enter filename (default: nursery_rhyme.txt): ")
   if len(filename) == 0 :
      filename = "nursery_rhyme.txt"
   inputFile = open(filename, "r")   

   for line in inputFile :
      theWords = line.split()
      for word in theWords :
         cleaned = clean(word)
         if cleaned != "" :
            uniqueWords.add(cleaned)

   print("The document contains", len(uniqueWords), "words.txt.")
   
## Cleans a string by making letters lowercase and removing characters 
#  that are not letters.
#  @param string the string to be cleaned
#  @return the cleaned string
#
def clean(string) : 
   result = ""
   for char in string :
      if char.isalpha() :
         result = result + char.lower()
         
   return result

# Start the program.
if __name__ == "__main__":
   main()