class DailyMessage:
    def __init__(self):
        self.message = ""
    def get_message(self):
        self.message = input("enter daily message: ")
    def print_message(self):
        print(self.message.upper())
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()
