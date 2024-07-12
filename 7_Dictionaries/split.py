# @copyright Deborah Kitchin

def main() -> None:
    # How to convert a string of values to a list.

    #1 enter values with space between
    line = input("Enter words with space between ")
    # Split the list of values when there is a space and put it in the list.
    words = line.split(" ")
    '''
    #2 enter values with any delimiter between
    delimiter = ";" # use whatever you want
    line = input(f"Enter words with {delimiter} between ")
    # Split the list of values when there is a space and put it in the list.
    words = line.split(delimiter)
    '''

    for word in words:
        print(word)


if __name__ == "__main__":
    main()
