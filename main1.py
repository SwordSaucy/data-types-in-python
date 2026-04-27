amount = float(input("enter purchased amount: "))
membership = input("do you have a membership answer with yes or no: ")
if amount >= 10000  or membership.lower() == "yes": 
    print("you have a discount")
else: 
    print("you do not have a discount")