try:
    a = float(input("enter number 1 for the opperation: "))
    b = float(input("enter number 2 for the operation: "))
except ValueError as e:
    print("you have entered an invalid input please enter a valid one")
except Exception as e:
    print("ERROR")
def add(e,f): 
    return(e+f)
def sub(e,f):
    return(e-f)
try:
    def div(e,f):
        return(e/f)
except ZeroDivisionError as e:
    print("Write a valid answer")
except Exception as e:
    print("ERROR")
def mul(e,f):
    return(e*f)
c = str(input("enter the operation you wish to complete: "))
if c.lower() == "multiplication":
    result=mul(a,b)
    print(f"the result is {result}")
if c.lower() == "subtraction":
    result=sub(a,b)
    print(f"the result is {result}")
if c.lower() == "addition":
    result=add(a,b)
    print(f"the result is {result}")
if c.lower() == "division":
    result=div(a,b)
    print(f"the result is {result}")