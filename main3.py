class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__ (self):
        return f"({self.x},{self.y})"
object1 = point(23,243)
print(object1)