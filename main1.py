class family:
    def __init__(self,eyecolor,height):
        self.eyecolor = eyecolor
        self.height = height
    def display(self):
        print(f"the eyecolor is {self.eyecolor} and the height is {self.height}")
class kid(family):
    def __init__(self,name,age,gender,eyecolor,height):
        #super().__init__(eyecolor,height)
        family.__init__(self,eyecolor,height)
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print(f"the name is {self.name}, the age is {self.age} and the gender is {self.gender}")
        super().display()
object = kid("zack",15,"male","blue",160)
object.display()
    