# customise the right ask whether car ride or bike ride if user takes bike ask unicycle or normal cycle then if the user picks car take if they are riding an suv or normal car
print("select your ride")
print("1. car")
print("2. bike")
a = int(input("enter your choice: "))
if a == 1: 
    print("select type of bike")
    print("1. scooti")
    print("2. scooter")
    b = int(input("enter your choice"))
    if b == 1: 
        print("you have selected scooti as your bike")
    elif b == 2: 
        print("you have selected the scooter as your choice")
    else: 
        print("you have selected an invaled choice")
if a == 2: 
    print("select type of car")
    print("1. suv")
    print("2. sudan")
    c = int(input("enter your choice"))
    if c == 2: 
        print("you have selected sudan as your car")
    elif c == 1: 
        print("you have selected the suv as your choice")
    else: 
        print("you have selected an invaled choice")
else: 
    print("you have selected an invaled choice overall")