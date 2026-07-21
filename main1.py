class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("constructor is called")
    def displayname(self):
        print(f"the employee name is {self.name}") 
    def displayagein10years(self):
        newage = self.age + 10
        print(f"the new age is {newage}")
    def __del__(self):
        print("destructer is called")
def createobject():
    print("making object")
    obj = employee("mark",32)
    print("function ends")
    return obj
print("create object function is called")
createobject()
print("program ends")