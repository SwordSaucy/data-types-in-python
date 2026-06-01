def addition(a,b): 
    sum = a+b
    return(sum)
def multi(a,b):
    plication = a*b
    return(plication)
def sub(a,b): 
    traction = a-b
    return(traction)
def div(a,b): 
    ision = a/b
    return(ision)
print("please select the operation")
print("1 for addtion \n 2 for multiplaction \n 3 for subtraction \n 4 for division")
choice= int(input("enter: "))
number1 = int(input("enter the first number"))
number2 = int(input("enter the second number"))
if choice == 1:
    print(f"the sum of {number1} and {number2} {addition(number1,number2)}")
elif choice == 4:
    print(f"the divide of {number1} and {number2} {div(number1,number2)}")
elif choice == 3:
    print(f"the substraction of {number1} and {number2} {sub(number1,number2)}")
elif choice == 2:
    print(f"the multiplication of {number1} and {number2} {multi(number1,number2)}")
else: 
    print("enter valid text")