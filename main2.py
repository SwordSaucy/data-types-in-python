#take 2 inputs from the user one of them is string and second is character then find out how many times the character is in the string
a = str(input("enter text:"))
b = str(input("character here"))
sum = 0
for i in a: 
    if b == i: 
        sum += 1
print(f"the amount of {b} characters in {a} is {sum}")