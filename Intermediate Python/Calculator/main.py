import os

def clear():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def addition(n1,n2):
    
    return n1+n2

def subtraction(n1,n2):
    
    return n1-n2

def multiply(n1,n2):
   
    return n1*n2

def divide(n1,n2):
    
    return n1/n2

num1=int(input("WHat s the first number= "))



start = True
while start:
    operate=str(input("""What operation you want

    +
    -
    *
    /
    """))
    num2=int(input("Write the second number = "))
    if operate == "+":
        result =addition(n1=num1,n2=num2)
    elif operate == "-":
        result= subtraction(n1=num1,n2=num2)
    elif operate == "*":
        result= multiply(n1=num1,n2=num2)
    else:
        result= divide(n1=num1,n2=num2)
    print(f"Your calculated number is {result}")
    condition = input("Do you want to continue with this number if yes type y if not type n").lower()
    if condition == "y":
        num1=result
    else:
        clear()
        num1=int(input("WHat s the first number= "))
        
        