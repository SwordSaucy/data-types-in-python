a = int(input("enter number 1(start)"))
b = int(input("enter number 2(end)"))
sum = 0
for i in range(a,b+1): 
    sum = sum+i
print(f"sum of numbers betwee {a} and {b} is {sum}")