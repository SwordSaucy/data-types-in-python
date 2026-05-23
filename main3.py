#while loop 
a = str(input("text"))
b = str(input("character"))
i = 0
sum = 0
while i < len(a): 
    if a[i] == b:
        sum += 1
    i += 1
print(f"the amount of {b} characters in {a} is {sum}")
    
    