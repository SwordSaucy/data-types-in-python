number = int(input("enter number: "))
def factorial(number): 
    if number == 0 or number == 1: 
        return 1
    else: 
        return number*factorial(number-1)
result = factorial(number)
print(f"the factorial of {number} is {result}")

