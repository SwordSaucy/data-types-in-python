#500,100,50,20,10,5,1
#% for remainder
#/ for division and double/ for floor division
a = int(input("enter a value: "))
b = a//500
c = a%500
d = c//100
e = c%100
f = e//50
g = e%50
h = g//20
i = g%20
j = i//10
k = i%10
l = k//5
m = k%5
n = m//1
print(f"you need {b} 500£ notes")
print(f"you need {d} 100£ notes")
print(f"you need {f} 50£ notes")
print(f"you need {h} 20£ notes")
print(f"you need {j} 10£ notes")
print(f"you need {l} 5£ notes")
print("you need " + str(n) + " 1£ notes")