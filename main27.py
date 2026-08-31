class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def show_details(self):
        print(f"brand: {self.brand}")
        print(f"max speed: {self.max_speed} mph")
class Car(Vehicle):
    def __init__(self, brand, max_speed, model, seats):
        super().__init__(brand, max_speed)
        self.model = model
        self.seats = seats
    def show_details(self):
        print(f"model: {self.model}")
        print(f"seats: {self.seats}")
        super().show_details()
    def fuel_type(self):
        print("fuel type: gasoline")
c = Car("Toyota", 120, "Camry", 5)
c.show_details()
c.fuel_type()
