amt=0
while True:
    print("\n===== MENU =====")
    print("1. deposit")
    print("2. withdrawl")
    print("3. check balance")
    print("4. interest calculator")
    print("5. Exit")
    

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            amt = int(input("Enter deposit amount: "))
            print("amount deposited",amt)

        case "2":
            if amt!=0:
              withd = int(input("Enter amount to withdraw: "))
              if withd < amt:
                  print("amount withdrawn!\nbalance left:",amt-withd)
              else:
                    print("low balance please add more amount")
            else:
                print("deposit first ")
                

        case "3":
            if amt!=0:
               print("total balance:", amt,"rs")
            else:
                print("first deposit amount")

        case "4":
            if amt !=0:
              p= int(input("enter principal amount:"))
              r= int(input("enter rate: "))
              t= int(input("enter time in years:"))
              si=(p*r*t)/100
              print("interest:",si,"rs")
            else:
                print("first deposit amount")

        case "5":
            print("Exiting Program...")
            break

        case _:
            print("Invalid Choice")