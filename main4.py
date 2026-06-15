import random as r
c = r.randint(1,20)
u = 0
lives = 6
while c != u:
    u = int(input("enter: "))
    if u > 20 or u < 1: 
        print("enter a valid number that is between 1 and 20 a life will not be lost")
        continue
    if u == c: 
        print("correct")
        break
    elif u > c: 
        lives = lives - 1
        print(f"value was higher than random number try again, you have {lives} lives")
    else: 
        print(f"value was lower than the random number try again, you have {lives} lives")
    if lives == 0:
        print(f"you have lost the answer was {c}")
        break
    