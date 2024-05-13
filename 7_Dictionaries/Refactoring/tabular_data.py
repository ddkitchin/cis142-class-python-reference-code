##
#  This module provides functions for working with tabular data 
#  consisting of lists of numbers, each of which has a name.
#

## Reads the tabular data.
#  @param filename name of the input file
#  @return a dictionary with the keys and data lists found in the file
#
def readData(filename:str) ->dict:
   # Create an empty dictionary.
   data = {}
   
   infile = open(filename, "r")
   
   # Read each record from the file.   
   for line in infile :
      fields = line.split(":")
      key = fields[0]
      data[key] = buildList(fields)

   infile.close()   
   return data

## Builds a list of values contained in the fields split from a string.
#  @param fields a list of strings comprising the record fields
#  @return a list of floating-point values
#
def buildList(fields:list) ->list:
   values = []
   for i in range(1, len(fields)) :
      sales = float(fields[i])
      values.append(sales)
      
   return values
   
## Prints a sales report.
#  @param data a table composed of a dictionary whose values are lists of numbers
#
def printReport(data:dict) ->None:
   # Find the number of columns as the length of the longest list.
   numColumns = 0
   for row in data.values() :
      if len(row) > numColumns :
         numColumns = len(row)

   # Create a list of column totals.
   columnTotals = [0.0] * numColumns
   
   # Print the key sales.
   for key in sorted(data) :
      print("%-20s" % key, end="")
      
      keyTotal = 0.0
      values = data[key]
      for i in range(len(values)) :
         value = values[i]
         keyTotal = keyTotal + value
         columnTotals[i] = columnTotals[i] + value
         print("%10.2f" % value, end="")

      print(" " * 10 * (numColumns - len(values)), end="")         
      print("%15.2f" % keyTotal)
         
   # Print the column totals.
   print("%20s" % " ", end="")
   for i in range(numColumns) :
      print("%10.2f" % columnTotals[i], end="")
   print()
   
