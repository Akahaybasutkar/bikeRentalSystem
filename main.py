import time
class BikeShop:

    hourlyPrice = 5
    dailyPrice = 20
    weeklyPrice = 60

    def __init__(self):
        self.bike_avl = 0
        print("Welcome to the shop")

    def addBikes(self, no):
        self.bike_avl += no
        print("Bikes added")
        self.checkBikes()

    def checkBikes(self):
        print(f"Available no of Bikes are: {self.bike_avl}")
        print()
        return self.bike_avl

    def rentBike(self, person, type="hourly"):
        if self.bike_avl > 1:
            person.start_time = time.perf_counter()
            self.bike_avl -= 1
            person.bikes_rented += 1
            person.current_rent_type = "hourly"
            print("Bike rented")

    def returnBike(self, person):
        person.end_time = time.perf_counter()
        total_time = (person.end_time - person.start_time) / 3600
        person.bikes_rented -= 1
        self.bike_avl += 1
        print("Bike returned")
        person.total_fare = total_time * 5
        person.checkBill()

class Person:

    def __init__(self, name):
        self.name = name
        self.bikes_rented = 0
        self.current_rent_type = None
        self.start_time = 0
        self.end_time = 0
        self.total_fare = 0

    def rentedBikes(self):
        print(f"You have rented {self.bikes_rented} bikes")
        return self.bikes_rented

    def info(self):
        print("Hello", self.name)
        print(f"Current rented bikes are: {self.bikes_rented}")
        pass
        print()

    def addBill(self, amount):
        print("Check1")
        self.bill += amount

    def checkBill(self):
        print("Your bill is: {:.2f}".format(self.total_fare))


p1 = Person("Akshay")
p1.info()

shop = BikeShop()
shop.addBikes(10)

shop.rentBike(p1, "hourly")
time.sleep(5)

shop.returnBike(p1)

