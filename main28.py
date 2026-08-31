class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = str(pin)
    def show_pin_status(self):
        print(f"for {self.owner}")
    def check_pin(self, user_pin):
        return str(user_pin) == self.__pin
    def set_pin(self, new_pin):
        new_pin_str = str(new_pin)
        if len(new_pin_str) == 4 and new_pin_str.isdigit():
            self.__pin = new_pin_str
            print("pin updated successfully")
        else:
            print("error: pin must be a 4-digit number")
    def __str__(self):
        return f"Account owner: {self.owner}"
my_account = Account("Alex", "1234")
print(my_account)
my_account.show_pin_status()
print("checking pin 1234:", my_account.check_pin("1234"))
my_account.__pin = "9999"
print("checking pin 9999 after direct update attempt:", my_account.check_pin("9999"))
print("checking pin 1234 after direct update attempt:", my_account.check_pin("1234"))
my_account.set_pin("9999")
print("checking pin 9999 after using set_pin:", my_account.check_pin("9999"))