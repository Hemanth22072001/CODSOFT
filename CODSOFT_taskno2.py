'''Function for Addition'''
def add(a,b):
    answer=a+b
    print(f'The addition operation of two digits are: {answer}','\n')

'''Function for Subtraction'''
def sub(a,b):
    answer=a-b
    print(f'The subtraction operation of two digits are: {answer}','\n')

'''Function for Multiplication'''
def mul(a,b):
    answer=a*b
    print(f'The multiplication operation of two digits are: {answer}','\n')

'''Function for Division'''
def div(a,b):
    answer=a/b
    print(f'The division operation of two digits are: {answer}','\n')

'''Function for Main Header'''
while True:
    print("\n---Calculator---")
    print("A.Addition(+)")
    print("B.Subtraction(-)")
    print("C.Multiplication(*)")
    print("D.Division(/)")
    print("E.Exit")

    m=input("Choose a number/operator to perform the arithematic operation: ")

    if m=='A' or m=='+':
        print("\n--Addition--")
        a=int(input("Enter the first digit: "))
        b=int(input("Enter the second digit: "))
        add(a,b)

    elif m=='B' or m=='-':
        print("\n--Subtraction--")
        a=int(input("Enter the first digit: "))
        b=int(input("Enter the second digit: "))
        sub(a,b)

    elif m=='C' or m=='*':
        print("\n--Multiplication--")
        a=int(input("Enter the first digit: "))
        b=int(input("Enter the second digit: "))
        mul(a,b)

    elif m=='D' or m=='/':
        print("\n--Division--")
        a=int(input("Enter the first digit: "))
        b=int(input("Enter the second digit: "))
        div(a,b)

    elif m=='E' or m=="exit":
        print("Thank You For Using The Calculator.")
        break

    else:
        print("Invalid Input.")