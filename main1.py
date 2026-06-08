a = int(input("enter the starting number"))
b = int(input("enter ending number"))
for i in range(a,b-1,-1):
    if i%5 == 0: 
        continue
    else: 
        print(i)