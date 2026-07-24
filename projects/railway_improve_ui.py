import random

seat_avail = 5
ticket_no = 0
name = ""
age = 0
gender = ""
source = ""
destination = ""
travel_class = ""
fare = 0
booked = False

while True:
    print("========🚆 welcome to the railway booking portal 🚆==========")
    print("1. book ticket 🎫")
    print("2. view ticket 👀")
    print("3. cancel ticket ❌")
    print("4. rate inquiry 💰")
    print("5. seat availability 💺")
    print("6. exit portal 🚪")
    ch = int(input("enter choice: "))

    match ch:
        case 1:
            if seat_avail > 0:
                if booked == True:
                    print("⚠️ you already have a ticket booked")
                    print("please cancel it before booking a new one")
                else:
                    name = input("enter name of the passenger: ")
                    age = int(input("enter age of the passenger: "))
                    gender = input("enter gender of the passenger: ")
                    source = input("enter the source to start journey: ")
                    destination = input("enter the destination: ")
                    travel_class = input("enter class type(general/AC/sleeper): ")
                    dist = int(input("enter distance in km: "))
                    travel_class.lower()
                    if dist > 0 and dist <= 100 and travel_class == "general":
                        fare = dist * 5
                    elif dist > 0 and dist <= 100 and travel_class == "ac":
                        fare = dist * 10
                    elif dist > 0 and dist <= 100 and travel_class == "sleeper":
                        print("🛌 for distance under 100km sleeper is not available")
                        print("booking as general instead")
                        fare = dist * 5
                    elif dist > 100 and dist <= 500 and travel_class == "general":
                        fare = dist * 5
                    elif dist > 100 and dist <= 500 and travel_class == "sleeper":
                        fare = dist * 10
                    elif dist > 100 and dist <= 500 and travel_class == "ac":
                        fare = dist * 15
                    elif dist > 500 and travel_class == "general":
                        fare = dist * 4
                    elif dist > 500 and travel_class == "sleeper":
                        fare = dist * 9
                    elif dist > 500 and travel_class == "ac":
                        fare = dist * 15
                    else:
                        print("⚠️ invalid distance or class, fare set to default")
                        fare = dist * 5

                    ticket_no = random.randint(1000, 9999)
                    seat_avail = seat_avail - 1
                    booked = True

                    print("✅ ticket booked successfully")
                    print("🎫 your ticket number is:", ticket_no)
                    print("💵 total fare is:", fare, "rupees")
            else:
                print("😔 no seats available")
                print("try again later....")

        case 2:
            if booked == True:
                print("=============🎫 TICKET 🎫============")
                print("ticket no  :", ticket_no)
                print("name       :", name)
                print("age        :", age)
                print("gender     :", gender)
                print("source     :", source)
                print("destination:", destination)
                print("class      :", travel_class)
                print("fare       :", fare, "rupees")
                print("======================================")
            else:
                print("😕 no ticket has been booked yet")

        case 3:
            if booked == True:
                chk = int(input("enter ticket no. to cancel ticket: "))
                if chk == ticket_no:
                    print("✅ your ticket has been canceled successfully")
                    seat_avail = seat_avail + 1
                    booked = False
                    ticket_no = 0
                    name = ""
                    age = 0
                    gender = ""
                    source = ""
                    destination = ""
                    travel_class = ""
                    fare = 0
                else:
                    print("❌ wrong ticket number")
                    print("try again...")
            else:
                print("😕 no ticket booked to cancel")

        case 4:
            dist = int(input("enter distance in km: "))
            category = input("enter class type(general/AC/sleeper): ")
            category.lower()
            if dist > 0:
                if dist <= 100 and category == "general":
                    print("💰 ticket price:", dist * 5, "rupees")
                elif dist <= 100 and category == "ac":
                    print("💰 ticket price:", dist * 10, "rupees")
                elif dist <= 100 and category == "sleeper":
                    print("🛌 for distance under 100km sleeper category is not available")
                    print("💰 ticket price for general is:", dist * 5, "rupees")
                    print("💰 ticket price for AC is:", dist * 10, "rupees")
                elif dist > 100 and dist <= 500 and category == "general":
                    print("💰 ticket price:", dist * 5, "rupees")
                elif dist > 100 and dist <= 500 and category == "sleeper":
                    print("💰 ticket price:", dist * 10, "rupees")
                elif dist > 100 and dist <= 500 and category == "ac":
                    print("💰 ticket price:", dist * 15, "rupees")
                elif dist > 500 and category == "general":
                    print("💰 ticket price:", dist * 4, "rupees")
                elif dist > 500 and category == "sleeper":
                    print("💰 ticket price:", dist * 9, "rupees")
                elif dist > 500 and category == "ac":
                    print("💰 ticket price:", dist * 15, "rupees")
                else:
                    print("⚠️ invalid class type entered")
            else:
                print("⚠️ enter valid distance")

        case 5:
            print("💺 total seats available:", seat_avail)
            bookseat = int(input("enter number of tickets you want: "))
            if bookseat <= seat_avail:
                print("✅ seats available")
            else:
                print("😔 seats not available")
                print("please try again later")

        case 6:
            print("=====🙏 thank you 🙏======")
            print("visit again later...... 🚆")
            break

        case _:
            print("⚠️ invalid choice try again....")