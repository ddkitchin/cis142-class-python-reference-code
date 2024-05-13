#@copyright Deborah Kitchin
from random import randint

def main()-> None:
    # Tuple example DOES NOT CHANGE AFTER DEFINED May see this, but not expected to use.
    rosterTuple = ("Debbie", "Nancy", "Amber", "Aricke", "Dylan", "Jeffery", "AJ")
    print(rosterTuple)

    storeSales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # I have 10 stores

    months = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]

    # I have a table of 10 stores with sales for each of the 12 months.
    monthSales = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print(storeSales)
    print(months)
    print(monthSales)
    storeTotal=0
    companyTotal=0
    for store in range(len(storeSales)):
        print("="*18,"Store",storeSales[store],"="*18)
        for month in range(len(months)):
            monthSales[store][month]=randint(0,100000)
            storeTotal=storeTotal+monthSales[store][month]
            print(f"\t\t\t{months[month]:10} {monthSales[store][month]:10}")
        print(f"\t\tStore Total {storeTotal:17}")
        companyTotal=companyTotal+storeTotal
        storeTotal=0
    print(f"\tCompany Total {companyTotal:23}")


if __name__ == "__main__":
    main()