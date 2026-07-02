amt=0; HRA=0
Da=0
x=0
while True:
    print("\n===== MENU =====")
    print("1. Enter Basic Salary")
    print("2. Calculate HRA(20%) and DA(10%)")
    print("3. Calculate net Salary")
    print("4. Tax Deduction")
    print("5. display salary slip")
    print("6. Exit")
    print("==================")
    
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            amt = int(input("enter basic salary: "))
            print("basic salary:",amt)
            print("---------------------")
        case "2":
            if amt!=0:
              HRA=amt*0.2
              Da=amt*0.1
              print("-----------------------------------------")
              print("HR Allowance(HRA):",HRA,"rs")  
              print("Dialy Allowance(DA):",Da,"rs")
              print("-----------------------------------------")
            else:
                print("enter basic salary first ")
                print("---------------------------------------")    

        case "3":
            if amt!=0:
               x=amt+Da+HRA
               print("---------------------------------------")
               print("Net Salary",x,"rs")
               print("---------------------------------------") 
            else:
                print("enter basic salary first")
                print("---------------------------------------")

        case "4":
            if amt !=0:
              taxr= int(input("enter tax rate in percent:"))
              tt=x*taxr/100
              x1=x-tt
              print("---------------------------------------")
              print("salary after tax deduction:", x1,"rs")
              print("---------------------------------------") 
            else:
                print("first deposit amount")
                print("---------------------------------------")
        case "5":
            print("----- Salary Slip -----")
            print("Basic Salary:",amt) 
            print("HRA: ",HRA)
            print("DA:",Da)
            print("Net Salary: ",x)
            print("Tax: ",tt)
            print("Final Salary:",x1)
            print("-----------------------")
            
        case "6":
            print("Exiting Program...")
            break

        case _:
            print("Invalid Choice")