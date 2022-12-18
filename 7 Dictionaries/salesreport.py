## 
#  This program processes a collection of sales data for flavors of ice cream
#  and prints a report sorted by flavor.
#

# Import a user-defined module that processes tabular data.
import tabulardata

filename = input("Enter sales data file name: ")
salesData = tabulardata.readData(filename)
tabulardata.printReport(salesData)
