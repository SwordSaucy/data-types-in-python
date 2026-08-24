class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"the name is {self.name} and the age is {self.age}")
class student(person):
    def __init__(self,grade,schoolname,name,age):
        person.__init__(self,name,age)
        self.schoolname = schoolname
        self.grade = grade
    def displaystudent(self):
        print(f"the schoolname is {self.schoolname} and the grade is {self.grade}")
        super().display()
object = student(9,"apple","james",23)
object.displaystudent()