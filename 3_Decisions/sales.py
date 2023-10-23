# @copyright Deborah Kitchin

def main():
    price = float(input("Enter price: "))

    if price < 28:
        discount = .92 # 8% discount
    else:
        discount = .84 # 16% discount

    finalPrice = price * discount

    print(f'Final price is ${finalPrice:.2f}.')

if __name__ == "__main__":
    main()