def main():
    print(fact(int(input("Enter an integer "))))
    
def fact(n):
    
    answer=1
    for i in range(0,n):
        answer=answer*(n-i)
        print("Line  9 answer=%d" %answer)
    print("Line 10 n=%d answer=%d" %(n, answer))
    return answer
    
main()