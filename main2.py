a = {"codingal":2,"is":2,"best":2,"for":2,"coding":1}
amount = 0
for i,j in a.items():
    if j == 2:
        amount = amount + 1
print(amount)