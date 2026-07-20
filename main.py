class student:
    def __init__ (self, name , age):
        self.name = name
        self.age = age
    def display(self):
        print(f"the name is {self.name}")
        print(f"the age is {self.age}")
object1 = student("mark",12)
object1.display()