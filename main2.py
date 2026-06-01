# take weather from the user and pass it to the function if user says it is sunny print it is summer if user says it is snowy print it is winter and if user says it is pleasent it is spring and if user says it is dry then print autumn

def climate(weather):
    if weather == "sunny": 
        print("it is summer")
    elif weather == "snowy": 
        print("it is winter")
    elif weather == "pleasent": 
        print("it is spring")
    elif weather == "dry": 
        print("it is autumn")
    else: 
        print("not a valid text")
a = input("how is the climate today: ")
climate(a)
