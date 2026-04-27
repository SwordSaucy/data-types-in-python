#take weight (kg) and height in (cm) from the user then alculate bmi using formula where bmi = weight / (height/100)**2. if bmi is less than 18.4 you are underwight/ unhealthy and if it less than 24.9 you are healthy if it is less than or equalt to 29.9 you are overweight, if it is less than or equal to 34.9 you are "overweight severey" if it is less than or equal to 39.9  you are obese. else you are severely obese
w = int(input("enter your weight in kg: "))
h = int(input("enter your weight in cm: "))
bmi = (w/(h/100)**2)
print(f"your bmi is {bmi}")
if bmi < 18.4: 
    print("your are underweight/ unhealthy")
elif bmi < 24.9: 
    print("you are healthy")
elif bmi <= 29.9: 
    print("you are overweight")
elif bmi <= 34.9: 
    print("you are severely overweight")
elif bmi <= 39.9: 
    print("you are obese")
else: 
    print("you are severely obese")
