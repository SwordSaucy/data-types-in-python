number = int(input("enter number: "))
factorial = 1
for i in range(number,0,-1): 
    factorial = factorial * i
print(f"the factorial of {number} is {factorial}")
