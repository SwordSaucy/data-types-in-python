name = input("enter username: ")
p = input("enter password: ")
if name.lower() == "admin" and p == "1234": 
    print("welcome")
else: 
    print("wrong please try again")