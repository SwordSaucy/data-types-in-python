a = (1,2,3,4,5,6,7,5,4,3,2,1)
length = len(a)
middle = length/2
b = 0
c = length-1
flag = True
while b < middle:
    if a[b] != a[c]:
        flag = False
    c = c-1
    b=b+1
if flag == True: 
    print("this is a pallendrome")
else: 
    print("not a pallendrome")