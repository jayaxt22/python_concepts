class Vehicle:

    def __init__(self, vehicle_number, brand, rent_per_day):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.rent_per_day = rent_per_day

    @property
    def rent_per_day(self):
        return self.__rent_per_day

    @rent_per_day.setter
    def rent_per_day(self, amount):
        if amount > 0:
            self.__rent_per_day = amount
        else:
            print("Invalid Rent Amount")

    @rent_per_day.deleter
    def rent_per_day(self):
        del self.__rent_per_day

    def display_vehicle(self):
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Brand          : {self.brand}")
        print(f"Rent Per Day   : {self.rent_per_day}")


class Car(Vehicle):

    def __init__(
        self,
        vehicle_number,
        brand,
        rent_per_day,
        number_of_seats
    ):
        super().__init__(
            vehicle_number,
            brand,
            rent_per_day
        )

        self.number_of_seats = number_of_seats

    def display_vehicle(self):
        super().display_vehicle()
        print(f"Number of Seats : {self.number_of_seats}")

    def calculate_rent(self, days):
        return self.rent_per_day * days


class Bike(Vehicle):

    def __init__(
        self,
        vehicle_number,
        brand,
        rent_per_day,
        engine_cc
    ):
        super().__init__(
            vehicle_number,
            brand,
            rent_per_day
        )

        self.engine_cc = engine_cc

    def display_vehicle(self):
        super().display_vehicle()
        print(f"Engine CC      : {self.engine_cc}")

    def calculate_rent(self, days):
        return self.rent_per_day * days