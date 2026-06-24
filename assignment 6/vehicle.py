vehicle = input("Enter vehicle type: ")
hours = int(input("Enter hours parked: "))

if vehicle == "Bike":
    fee = hours * 10
elif vehicle == "Car":
    fee = hours * 20
else:
    fee = hours * 50

if hours > 5:
    fee += 100

print("Total Parking Fee:", fee)