##
#  This program checks which words in a file are not present in a list of
#  correctly spelled words.
#

# Import the split function from the regular expression module.
from re import split

def main() :
   # Read the word list and the document.
   correctlySpelledWords = readWords("words")
   documentWords = readWords("alice30.txt")

   # Print all words that are in the document but not the word list.
   misspellings = documentWords.difference(correctlySpelledWords)
   for word in sorted(misspellings) :
      print(word)
   
## Reads all words from a file.
#  @param filename the name of the file
#  @return a set with all lowercased words in the file. Here, a word is a 
#  sequence of upper- and lowercase letters
#   
def readWords(filename) :
   wordSet = set()
   inputFile = open(filename, "r")
   
   for line in inputFile :
      line = line.strip()
      # Use any character other than a-z or A-Z as word delimiters.
      parts = split("[^a-zA-Z]+", line)
      for word in parts :
         if len(word) > 0 :
            wordSet.add(word.lower())
            
   inputFile.close()
   return wordSet
   
# Start the program.
main()
