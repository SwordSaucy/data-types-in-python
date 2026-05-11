a = int(input("enter a number: "))
if a >= 0: 
    if a %2 == 0: 
        print("the number is positive and positive")
    else: 
        print("this number is odd and positive")
else: 
    if a %2 == 0: 
        print("the number is positive and negative")
    else: 
        print("this number is odd and negative")
    