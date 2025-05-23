class vehical:
    def __init__(self,types):
        self.types = types
    def display_vehival(self):
        print(f"Vehical Type: {self.types}")
class Car(vehical):
    def __init__(self,types,car_type):
        super().__init__(types)
        self.car_type = car_type
    def display_car(self):
        self.display_vehival()
        print(f"Car type: {self.car_type}")
class Electric(Car):
    def __init__(self,types,car_type,price):
        super().__init__(types,car_type)
        self.price = price
    def display_ele(self):
        self.display_car()
        # print(f"vehical: {self.types}")
        # print(f"Car type: {self.car_type}")
        print(f"price: {self.price}")

v = Electric("Car","Electric",3500000)
v.display_ele()