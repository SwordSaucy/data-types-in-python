#take math and science score from the user. if total of score is greater to or equal to hundred then they passed. the user also passed in individual subject if score is greater than 40 else they failed
math = int(input("enter your math score out of 100: "))
science = int(input("enter your science score out of 100: "))
if (math + science >= 100) and (math > 40 or science > 40): 
    print("you have passed")
else: 
    print("you have failed")