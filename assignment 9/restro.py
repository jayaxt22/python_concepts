amount = 2500
customer_type = "VIP"
payment = "online"

if amount >= 2000:
    if customer_type == "VIP":
        if payment == "online":
            print("Offer = Free Dessert + 20% Discount")
        else:
            print("Offer = Free Dessert")
    else:
        if amount >= 5000:
            print("Offer = 15% Discount")
        else:
            print("Offer = 10% Discount")

else:
    if amount >= 1000:
        if customer_type == "VIP":
            print("Offer = 10% Discount")
        else:
            print("Offer = 5% Discount")
    else:
        print("Offer = No Offer")