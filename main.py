pencilbox = ["pencil", "eraser", "ruler","calulator", "pen"]
amount = [1,0,4,2,0]
a = {key:value for key,value in zip(pencilbox,amount)}
print(a)
stock = [x for x in pencilbox if a[x] > 0]
print(stock)
userinput = str(input("enter the thing you wish to buy!: "))
if userinput not in pencilbox or a[userinput] == 0:
    print("not in stock")
    exit()