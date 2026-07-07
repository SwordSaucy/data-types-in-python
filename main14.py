a = input("enter yes or no: ")
def shutdown(user_input):

    if user_input.lower() == "yes":
        print("shutting down")
    
    elif user_input.lower() == "no":
        print("abort shut down")

    else:
        print("sorry.")

shutdown(a)