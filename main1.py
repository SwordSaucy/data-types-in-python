prices = [1,2,4,2,4,1,2]
userinput = int(input("enter a markup amount:"))
markup = list(map(lambda x: x + userinput, prices))
print(markup)