try:
    number1 = int(input("enter number 1: "))
    number2 = int(input("enter number 2: "))
    print(number1/number2)
except ValueError as e:
    print("please enter a number")
except ZeroDivisionError as e:
    print("a number cannot be divided by 0")
except SyntaxError as e:
    print("please enter and integer")
except:
    print("please check your code")
finally:
    ("im in finally")