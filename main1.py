class fruit:
    def __init__(self, name, ripe):
       self.name = name 
       self.ripe = ripe
    def display(self):
        print(f"the name is {self.name}")
        print(f"the fruit is {self.ripe}")
object = fruit("strawberry","purple")
object1 = fruit("mango","purple")
object.display()
object1.display()