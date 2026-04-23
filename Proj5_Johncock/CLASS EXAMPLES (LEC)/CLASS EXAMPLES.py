import random
def multiply():
    a = random.randint (0,9)
    b= random.randint (0,9)
    return a,b


def main():
    x,y= multiply()

    print(f'{x} multiplied by {y}')
    answer=int(input("your answer: "))
    right_answer= x*y
    if answer == right_answer:
        print('CORRECT!')
    
    else:
        print('WRONG BITCH TRY AGAIN')

if __name__=='__main__':
    main()