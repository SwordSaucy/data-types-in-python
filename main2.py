from abc import ABC,abstractmethod
class animal():
    @abstractmethod
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
    def move(self):
        print("i can move")
class lion(animal):
    def move(self):
        print("i can roar")
objlion = lion()
objdog = dog()
objsnake = snake()
objhuman = human()
objhuman.move()
objlion.move()
objdog.move()
objsnake.move()