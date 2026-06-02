#i want to create a function to calculate tip paid to waiter. function has 2 arguments bills and tips% using calculate tip and print it taken from user

def tippercentage(bills,tip):
    a = tip/100 
    tipamount = bills*a
    print(f"the amount that is to be paid is {bills+tipamount}")
bills = int(input("please enter the total bill: "))
tip = int(input("please enter the tip amount in %: "))
tippercentage(bills,tip)