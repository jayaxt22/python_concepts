travel_class = "economy"
distance = 1200
booking = "early"

if travel_class == "business":
    if distance > 1000:
        price = 8000
    else:
        price = 5000

else:
    if distance > 1000:
        if booking == "early":
            price = 4000
        else:
            price = 5000
    else:
        price = 2500

print("Ticket Price =", price)