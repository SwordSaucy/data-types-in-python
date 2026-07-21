class iosstring:
    def __init__(self):
        self.string1 = ""
    def getstring(self):
        self.string1 = str(input("asign here"))
    def display(self):
        print(f"string is{self.string1}")
obj = iosstring()
obj.getstring()
obj.display()