
============================================================
ASSIGNMENT 3 — VEHICLE RENTAL SYSTEM
====================================


A vehicle rental company rents different types of vehicles.

Create:

Vehicle
|
+-------- Car
|
+-------- Bike

REQUIREMENTS:

1. Create Vehicle class.

Attributes:

* vehicle_number
* brand
* rent_per_day

2. Car should inherit from Vehicle.

Additional:

* number_of_seats

3. Bike should inherit from Vehicle.

Additional:

* engine_cc

4. Initialize parent data using super().

5. Create:

display_vehicle()
calculate_rent(days)

6. Override calculate_rent() in Car and Bike.

7. The child methods must call the parent calculation using super().

8. Use a property for rent_per_day.

9. Create:

@property
@rent_per_day.setter
@rent_per_day.deleter

10. rent_per_day must be greater than 0.

11. Read all information from the user.

INPUT:

Enter Vehicle Number:
Enter Brand:
Enter Rent Per Day:
Enter Vehicle Type:

1. Car
2. Bike

If Car:

Enter Number of Seats:

If Bike:

Enter Engine CC:

Enter Number of Rental Days:

SAMPLE INPUT:

Enter Vehicle Number: MP09AB1234
Enter Brand: Hyundai
Enter Rent Per Day: 1500
Enter Vehicle Type: 1
Enter Number of Seats: 5
Enter Number of Rental Days: 4

EXPECTED OUTPUT:

## Vehicle Details

Vehicle Number: MP09AB1234
Brand: Hyundai
Rent Per Day: 1500
Vehicle Type: Car
Number of Seats: 5

Rental Days: 4
Total Rent: 6000