list1= ["aba", "cfc", "xyz", "abc", "121"]
count = 0
for i in list1: 
    if i[0] != i[-1]: 
        continue
    else: 
        count = count + 1
print(count)
