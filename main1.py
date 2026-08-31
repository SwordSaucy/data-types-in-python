#create 2 classes of any 2 countries in each class have 3 functions (capital language and type)
class england():
    def capital(self):
        print("the capital is london")
    def language(self):
        print("the language spoken is english")
    def type(self):
        print("the country is developed")
class china():
    def language(self):
        print("the language spoken is mandarin")
    def type(self):
        print("the country is developed")
    def capital(self):
        print("the capital is Beijing")
obj1 = england()
obj2 = china()
for i in (obj1,obj2):
    i.language()
    i.capital()
    i.type()