#check exaM ELIGIBILITY take input from the user regarding medical issues, if yes you are allowed else ask attendance percentage if > 75 you are allow else no
a = str(input("do you have a medical issue if yes enter yes and if no enter no: "))
if a.lower() == "yes": 
    print("you are allowed to resit the exam")
else: 
    b = int(input("enter in you attendance percentage score to test eligibility"))
    if b >= 75: 
        print("you are allowed to resit the test")
    else: 
        print("you are not allowed to resit the test")
    