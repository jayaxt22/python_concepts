from models.vehicle import Car, Bike
from rich.prompt import Prompt


vehicle_number = input("Enter Vehicle Number : ")
brand = input("Enter Brand : ")
rent_per_day = int(input("Enter Rent per Day : "))

print("Choose Vehicle Type")
print("1. Car")
print("2. Bike")

choice = Prompt.ask(
    "Enter Vehicle Type",
    choices=["1", "2"]
)


if choice == "1":

    number_of_seats = int(
        input("Enter Number of Seats :")
    )

    car = Car(
        vehicle_number,
        brand,
        rent_per_day,
        number_of_seats
    )

    days = int(
        input("Enter Number of Days : ")
    )

    car.display_vehicle()

    print(
        f"Total Rent : {car.calculate_rent(days)}"
    )


else:

    engine_cc = int(
       input("Enter Engine CC : ")
    )

    bike = Bike(
        vehicle_number,
        brand,
        rent_per_day,
        engine_cc
    )

    days = int(
       input("Enter Number of Days : ")
    )

    bike.display_vehicle()

    print(
        f"Total Rent : {bike.calculate_rent(days)}"
    )