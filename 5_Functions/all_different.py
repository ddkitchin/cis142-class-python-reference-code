def main()-> None:
    print(f'With values 1 1 1, answer should be False. Answer is {allDifferent(1,1,1)}.')
    print(f'With values 1 1 2, answer should be False. Answer is {allDifferent(1,1,2)}.')
    print(f'With values 1 2 2, answer should be False. Answer is {allDifferent(1,2,2)}.')
    print(f'With values 2 1 2, answer should be False. Answer is {allDifferent(2,1,2)}.')
    print(f'With values 1 2 3, answer should be True.  Answer is {allDifferent(1,2,3)}.')
    
# @return different indicating if 3 variables are different
def allDifferent(value1:int, value2:int, value3:int)-> bool:
    
    '''This next line is the same result as lines 13-16
    return value1 != value2 and value2 != value3 and value1 != value3'''
    
    different = False
    if (value1 != value2 and value1 != value3 and value2 != value3):
        different = True
    return different

if __name__ == "__main__":
    main()