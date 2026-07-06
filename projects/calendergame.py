while True:
    ch=int(input("========WELCOME========\n1: press 1 for calender related calculations.\n2: press 2 fro clock related operations\nenter choice: "))
    match ch:
        case 1:
            print("you have chosen calender related operation")
            print("\n===== MENU =====")
            print("1.find the day of entered date.")
            print("2. ")
            print("3. how many days from date A to date B")
            print("4. check whether a year is leap or not")
            print("5. Exit")
            ch1= int(input("enter your choice: "))
            while True:
                match ch1:
                   case 1:
                       print("")
                   case 2:
                       print("")
                   case 3:
                       print("")
                   case 4:
                       print("")
                   case 5:
                       print("exited......")
                       break
                   case __:
                       print("invalid input")
        case 2:
            print("you have chosen clock related operations...")
            
            print("\n===== MENU =====")
            print("1.find the day of entered date.")
            print("2. ")
            print("3. how many days from date A to date B")
            print("4. check whether a year is leap or not")
            print("5. Exit")
        case __:
            break
                