#if the number is divisable by 20 it provides an output twist if the number is divisable by 15 it will not give any output  annd if number is diivisable by 5 it should print fizz and if number is divisable by 3 it will give buzz else ouput is as number itself
a = int(input("enter the starting number"))
b = int(input("enter the ending number"))
for i in range(a,b+1): 
    if i%20 == 0: 
        print("twist")
        continue
    if i%15 == 0:
        continue
    if i%5 == 0: 
        print("fizz")
        continue
    if i%3 == 0: 
        print("buzz")
        continue
    else: 
        print(f"{i}")