num1=input(int("Enter the fist number: "))
num2=input(int("Enter the second number: "))
operation= input("Choose the operation (+, -, *, /): ")
match operation:
    case '+':
        print("The result is",num1+num2)
    case '-':
        print("The result is",num1-num2)
    case '*':
        print("The result is",num1*num2)
    case '/':
        if num2!=0:
            print("The result is",num1/num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("invalid operator")