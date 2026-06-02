# create one function to calculate ^3 , create a second function to check if number is / by 3 or not and if yes then call cube function
def power3(number): 
    a = number*number*number
    print (f"{number} to the power of 3 is {a}")
def div(number):
    if number%3 == 0: 
        power3(number)
        print("your number is divisable by 3")
    else: 
        print("your number is not divisable by 3")
number = int(input("please enter the number: "))
div(number)