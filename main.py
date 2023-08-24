import time
from timeit import default_timer as timer


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

    def rentBike(self, person, bikes):
        """Used to rent bikes \nTakes parameter Person(Object), No of Bikes needed, type of rent
        :param person:
        :param bikes:
        :param type:
        :return:
        """
        if self.bike_avl >= 1 and self.bike_avl >= bikes:
            ask = input("Enter the type of rental(hourly, daily, weekly): \n")

            if ask.lower() == "hourly":
                person.current_rent_type = "hourly"
                person.start_time = timer()
                person.bikes_rented += bikes
                self.bike_avl -= bikes

            elif ask.lower() == "daily":
                person.current_rent_type = "daily"
                person.start_time = timer()
                person.bikes_rented += bikes
                self.bike_avl -= bikes

            elif ask.lower() == "weekly":
                person.current_rent_type = "weekly"
                person.start_time = timer()
                person.bikes_rented += bikes
                self.bike_avl -= bikes

            elif ask.lower() == "family":
                person.current_rent_type = "weekly"
                person.start_time = timer()
                person.bikes_rented += bikes
                self.bike_avl -= bikes

            else:
                print("Wrong rental type entered!!!")

        else:
            print("Bikes not available\nSorry for inconvenience")

    def familyRental(self, person, bikes):

        """Used to rent bikes \nTakes parameter Person(Object), No of Bikes needed, type of rent
        :param person:
        :param bikes:
        :param type:
        :return:
        """
        if self.bike_avl >= 1 and self.bike_avl >= bikes:
            person.isFamily = True
            ask = input("Enter the type of rental(hourly, daily, weekly): \n")

            if ask.lower() == "hourly":
                person.current_rent_type = "hourly"
                person.start_time = timer()
                person.bikes_rented += bikes
                self.bike_avl -= bikes
                print("Bike rented")

            elif ask.lower() == "daily":
                person.current_rent_type = "daily"
                person.start_time = timer()
                person.bikes_rented += bikes
                self.bike_avl -= bikes
                print("Bike rented")

            elif ask.lower() == "weekly":
                person.current_rent_type = "weekly"
                person.start_time = timer()
                person.bikes_rented += bikes
                self.bike_avl -= bikes
                print("Bike rented")

            else:
                print("Wrong rental type entered!!!")

        else:
            print("Bikes not available\nSorry for inconvenience")

    def returnBike(self, person):

        if person.current_rent_type == "hourly":
            person.end_time = timer()
            person.time = person.end_time - person.start_time
            person.total_fare = ((person.time / 3600) * 3600) * person.bikes_rented

        elif person.current_rent_type == "daily":
            person.end_time = timer()
            person.time = person.end_time - person.start_time
            person.total_fare = ((person.time / (24 * 3600)) * 20) * person.bikes_rented

        elif person.current_rent_type == "weekly":
            person.end_time = timer()
            person.time = person.end_time - person.start_time
            person.total_fare = ((person.time / (7 * 24 * 3600)) * 60) * person.bikes_rented

        if person.isFamily:
            person.total_fare *= 0.7

        print("Bike returned.")
        person.checkBill()

        if person.bikes_rented == 0:
            person.total_fare = 0


class Person:

    def __init__(self, name):
        self.name = name
        self.bikes_rented = 0
        self.current_rent_type = None
        self.start_time = 0
        self.end_time = 0
        self.time = 0
        self.total_fare = 0
        self.isFamily = False

    def rentedBikes(self):
        print(f"You have rented {self.bikes_rented} bikes")
        return self.bikes_rented

    def info(self):
        print("Hello", self.name)
        print(f"Current rented bikes are: {self.bikes_rented}")
        print("Your Bill is: {:.2f}".format(self.total_fare))
        print()

    def checkBill(self):
        print("Your bill is: ${:.2f}".format(self.total_fare))

    def payBill(self, amount):

        if self.total_fare > amount:
            self.total_fare -= amount
        else:
            print("Amount greater tha pending amount")


shop = BikeShop()
p1 = Person("Akshay")
shop.addBikes(10)

shop.familyRental(p1, 2)
time.sleep(5)
shop.returnBike(p1)
p1.info()
