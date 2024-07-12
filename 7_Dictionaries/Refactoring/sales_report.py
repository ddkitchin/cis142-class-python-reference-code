## 
#  This program processes a collection of sales data for flavors of ice cream
#  and prints a report sorted by flavor.
#

# Import a user-defined module that processes tabular data.
import tabular_data


def main() -> None:
    filename = input("Enter sales data file name: ")
    salesData = tabular_data.readData(filename)
    tabular_data.printReport(salesData)


if __name__ == "__main__":
    main()
