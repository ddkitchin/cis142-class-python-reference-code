# @copyright Deborah Kitchin

def main():
    # set i to a value. Try 1, 3, 0, 4, and 10
    i = 1

    # set contant. Try, 3, -1, 10
    LIMIT = 3

    # How many times is while boolean tested?
    while (i <= LIMIT):
        print(f'i = {i}')
        i = i + 1  # this is a valid accumualtor and same result as next line.
        # i += 1  # this is a valid accumualtor and same result as previous line.

    print("finished")
    print(f'i = {i}')


if __name__ == "__main__":
    main()
