demand = 85
stock = 40
user_type = "premium"
festival = "yes"

if demand >= 80:
    if stock < 50:
        if user_type == "premium":
            if festival == "yes":
                print("Discount = 20%")
            else:
                print("Discount = 10%")
        else:
            print("Discount = 0%")
    else:
        print("Discount = 5%")

elif demand >= 40:
    if festival == "yes":
        print("Discount = 10%")
    else:
        print("Discount = 0%")

else:
    if stock > 200:
        print("Discount = 15%")
    else:
        print("Discount = 0%")