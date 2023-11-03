class Car:
    brand = None
    model = None
    year = None
    color = None
    fuel = None

    def start(self):
        print(f"Car has {self.color} color and year {self.year} and is starting")

    def brand_print(self):
        print(f"Car brand is {self.brand} ")

    def get_info(self):
        print(f"car properties are as under : brand = {self.brand}, model = {self.model}, year = {self.year}, color = {self.color}, fuel = {self.fuel}")

    def turn_left(self):
        print(f"car {self.brand} has smooth turning left specially")

    def steering(self):
        print(f"car {self.brand} has smooth steering")

obj1 = Car()
obj1.brand = "toyota"
obj1.model = "Etios"
obj1.year = "2000"
obj1.color = "red"
obj1.fuel = "diesel"

obj2 = Car()
obj2.brand = "maruti"
obj2.model = "swift"
obj2.year = "2022"
obj2.color = "white"
obj2.fuel = "petrol"

print("Calling ======= Obj1 methods ========")
obj1.start()
obj1.brand_print()
obj1.get_info()
obj1.turn_left()
obj1.steering()

print("\n ===== calling obj2 methods =======")
obj2.start()
obj2.brand_print()
obj2.get_info()
obj2.turn_left()
obj2.steering()