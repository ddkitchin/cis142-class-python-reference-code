# @copyright Deborah Kitchin

def main() -> None:
    limit = int(input("Count from 1 to what number? "))

    print("for i in range (limit) :")
    for i in range(limit):
        print(i, end=" ")
    print()

    print("for i in range (0,limit) :")
    for i in range(0, limit):
        print(i, end=" ")
    print()

    print("for i in range (0, limit, 2):")
    for i in range(0, limit, 2):
        print(i, end=" ")
    print()

    print("for i in range (limit, 0, -2):")
    for i in range(limit, 0, -2):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
