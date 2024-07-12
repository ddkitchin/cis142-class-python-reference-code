## 
#  This program tests the CashRegister class.
#

from CashRegister import CashRegister


def main() -> None:
    register1 = CashRegister()
    register1.addItem(1.95)
    register1.addItem(0.95)
    register1.addItem(2.50)

    print('*****Register 1******')
    print(f"Expected Count : 3     Actual   : {register1.getCount()}")
    print(f"Expected Total : 5.40  Actual   : {register1.getTotal():.2f}")

    print('*****Register 2******')
    register2 = CashRegister()
    register2.addItem(1)
    register2.addItem(2)

    print(f"Expected Count : 2     Actual   : {register2.getCount()}")
    print(f"Expected Total : 3.00  Actual   : {register2.getTotal():.2f}")
    register2.clear()
    print(f"Expected Count : 0     Actual   : {register2.getCount()}")
    print(f"Expected Count : 0.00  Actual   : {register2.getTotal():.2f}")

    print('*****Register 3 Tax ******')
    register3 = CashRegister(10)  #10 percent tax rate
    register3.addItem(1.00)
    register3.addItem(10.00, True)

    print(f"Expected : Count 2     Actual   : {register3.getCount()}")
    print(f"Expected : Count 12.00 Actual   : {register3.getTotal():.2f}")


if __name__ == "__main__":
    main()
