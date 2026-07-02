units = None
bill = 0
surcharge = 0

while True:
    print("\n===== Electricity Bill Management System =====")
    print("1. Enter Units Consumed")
    print("2. Calculate Bill Amount")
    print("3. Apply Surcharge")
    print("4. Display Final Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            units = int(input("Enter units consumed: "))
            print("Units recorded successfully")

        case "2":
            if units is None:
                print("Please enter units consumed first")
            else:
                if units <= 100:
                    bill = units * 5
                elif units <= 200:
                    bill = (100 * 5) + ((units - 100) * 7)
                else:
                    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

                print("Bill Amount:", bill)

        case "3":
            if units is None:
                print("Please enter units consumed first")
            elif bill == 0:
                print("Please calculate bill amount first")
            else:
                if bill > 2000:
                    surcharge = bill * 10 / 100
                else:
                    surcharge = bill * 5 / 100

                print("Surcharge:", surcharge)

        case "4":
            if units is None:
                print("Please enter units consumed first")
            elif bill == 0:
                print("Please calculate bill amount first")
            else:
                print("\n----- Final Bill -----")
                print("Units:", units)
                print("Bill Amount:", bill)
                print("Surcharge:", surcharge)
                print("Total Payable:", bill + surcharge)

        case "5":
            print("Exiting system... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")