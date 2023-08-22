import datetime as dt
import time

class BikeShop:

    hourlyPrice = 5
    dailyPrice = 20
    weeklyPrice = 60

    def __init__(self, bikes=0):
        self.bike_avl = bikes
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.fare = 0

    def addBikes(self, no):
        self.bike_avl += no
        print("Bikes added")
        print("The number of bikes available are: ", self.checkBikes())

    def checkBikes(self):
        print(f"Available no of Bikes are: {self.bike_avl}")
        return self.bike_avl

    def rentBike(self, person, type="hourly"):

        if self.checkBikes() > 1:
            if type.lower() == "hourly":
                print(f"The rental for hourly basis is: ${BikeShop.hourlyPrice}")
                ct = input("Would you like to continue?")

                if ct.lower() == "yes":
                    self.start_time = time.perf_counter()
                    person.bikes_rented += 1
                    self.bike_avl -= 1

    def returnBike(self, person, type="hourly"):
        print("Bike returned. Your fare is being calculated")
        self.end_time = time.perf_counter()
        self.total_time = self.end_time - self.start_time
        # self.billing(person, type)
        person.bikes_rented += 1

    def billing(self, person, type="hourly"):

        if type.lower() == "hourly":
            self.fare = (self.total_time * 3600) * 5
        print("Your fare is: ", self.fare)
        person.self.bill += int(self.fare)
        return self.fare


class Person:

    def __init__(self, name):
        self.name = name
        self.bikes_rented = 0
        self.rent_history = []
        self.bill = 0

    def rentedBikes(self):
        print(f"You have rented {self.bikes_rented} bikes")
        return self.bikes_rented


p1 = Person("Akshay")
shop = BikeShop(10)
shop.checkBikes()
shop.rentBike(p1, "hourly")
time.sleep(3)

p1.rentedBikes()
print("Here")
shop.checkBikes()
shop.returnBike(p1, "hourly")
shop.checkBikes()
