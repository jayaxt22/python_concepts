#nested if else 
unit = int(input("enter unit consumed: "))
if unit>= 100:
    if unit>= 300:
        print("usage category = High Usage")
    else:
        if unit>=200:
            print("usage category = Moderate Usage")
        else:
            print("usage category = Normal Usage")
else:
    print("usage category = Low Usage")
            

