
class student:
    __passingmarks = 40
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__privatevariable = 100
    def display(self):
        print(f"the name is {self.name} the age is{self.age}")
        print(f"private variable is {self.__privatevariable}")
    def displaypassingmarks(self):
        print(f"the passing marks are {student.__passingmarks}")
object1 = student("jhon",23)
object1.display()
object1.displaypassingmarks()
object1.__passingmarks = 32   
object1.displaypassingmarks()
#print(f"the private variable is {object.__privatevariable}") 
