def main():
    print(fact(int(input("Enter an integer "))))
    
def fact(n):
    print("Line  5 n=%d" %n)
    if n == 0:
        return 1
    else:
        answer= fact(n-1)*n
        print("Line 10 n=%d answer=%d" %(n, answer))
        return answer
    
if __name__ == "__main__":
    main()