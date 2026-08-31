from abc import ABC,abstractmethod
class veichle():
    def displaycolor(self):
        print("the color is red")
    def wheelsize(self,size):
        print("the size is: ", size)
    @abstractmethod
    def maximumspeed(self):
        print("the maximumspeed is 150kmph")
class gt5(veichle):
    def maximumspeed(self):
        print("the maximum speed is 234kmph")
obj1 = gt5()
obj1.maximumspeed()
obj1.displaycolor()
obj1.wheelsize(34)
