class Car:

    def __init__(self, brand, model, distance, fuel_consumed,
                 petrol_price):
        self.brand = brand
        self.model = model
        self.distance = distance
        self.fuel_consumed = fuel_consumed
        self.petrol_price = petrol_price
        self.mileage=0
        self.fuel_cost=0

    def calculate_mileage(self):
        self.mileage=self.distance / self.fuel_consumed
        return self.mileage

    def calculate_fuel_cost(self):
        self.fuel_cost= self.fuel_consumed * self.petrol_price
        return self.fuel_cost

    def display_trip_details(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Distance Travelled:", self.distance, "km")
        print("Fuel Consumed:", self.fuel_consumed, "litres")
        print("Petrol Price:", self.petrol_price)
        print("Mileage:", self.mileage, "km/l")
        print("Fuel Cost:", self.fuel_cost)


# Create object
car = Car("Maruti", "Swift", 320, 20, 105)


car.calculate_mileage()
car.calculate_fuel_cost()
car.display_trip_details()