class pet:
    print("has run")
pet_object = pet()
class petprofile:
    category = "pet"
    def __init__(self,name,animal,age,feed):
        self.name = name
        self.animal = animal
        self.age = age
        self.feed = feed
pet1 = petprofile("dave","fish",1.5,"fish_food")
pet2 = petprofile("harry","turtle",64,"dave")
print("harry favourite food is", pet2.feed)
print("dave is", pet1.age, "years old")