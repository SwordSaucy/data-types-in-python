def displaymessage(message): 
    if message == "hi": 
        print("good morning")
    elif message == "bye" or message == "goodbye": 
        print("goodnight")
    else: 
        print("please enter somethng better")
a = input("text: ")
displaymessage(a)