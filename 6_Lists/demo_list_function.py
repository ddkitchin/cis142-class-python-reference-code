# @copyright Deborah Kitchin

def main()-> None:
    # created a list of 3 items
    l = ["a", "b", "c"]
    print("List before function", l)
    # called function with list as parameter
    demoListFunction(l)
    print("List after function", l)

def demoListFunction(l:list)-> None:
    
    print("\tList in function", l)
    
    # change first item in list
    l[0] = "z"
    print("\tList in function after first item changed", l)

    # create new list with numbers and sent l to new list
    newL = [1, 2, 3]
    l = newL
    print ("\tList in function after set to new list", l)

if __name__ == "__main__":
    main()
