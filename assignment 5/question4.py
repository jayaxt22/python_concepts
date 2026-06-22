bal = int(input("enter balance amount:"))
amt = int(input ("enter amount to withdraw:"))
PIN = int(input("enter pin:"))
if bal >= amt:
    if amt>=10000:
       print("transaction limit exceeded")
    else:
       if PIN == 1234:
        print("withdrawal successful")
       else:
        print("incorrect pin")
else:
    print("insufficient balance")