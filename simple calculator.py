#Winni Lu
#11/19/24
#simple calculator
#init
#functions
def add(num1, num2): #adds the given numbers
    result=num1+num2
    print("The reuslt is " +str(result))
def subtract(num1,num2): #subtracts the given numbers
    result=num1-num2
    print("The result is "+str(result))
def multiply(num1,num2): #multiplies the given numbers
    result=num1*num2
    print("The result is "+str(result))
def divide(num1,num2): #divides the given numbers
    result=num1/num2
    print("The result is "+str(result))
def simple_calculator():
    print("Welcome to Simple Calculator") #introduces the program
    while True:
        print("Select an operation: ") #asks for the user to choose an operation
        print("""1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Quit""")
        option=int(input("(1-5) Select option: "))
        if option == 1 :
            int1=int(input("Enter first number: "))
            int2=int(input("Enter second number: "))
            add(int1,int2)
        if option == 2 :
            int1=int(input("Enter first number: "))
            int2=int(input("Enter second number: "))
            subtract(int1,int2)
        if option == 3 :
            int1=int(input("Enter first number: "))
            int2=int(input("Enter second number: "))
            multiply(int1,int2)
        if option == 4 :
            int1=int(input("Enter first number: "))
            int2=int(input("Enter second number: "))
            divide(int1,int2)
        if option ==5:
            break
#main
simple_calculator()
