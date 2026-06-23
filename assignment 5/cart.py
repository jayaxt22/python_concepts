#nested if else 
cart = int(input("enter your cart value: "))
cred = input("enter user type(premium/reguler: ")  
cred = cred.lower()
if cart>=5000:
    if cred == "premium":
        print("final amount= ",cart-(cart *20/100),"rs")
    else:
        if cred == "reguler":
             print("final amount= ",(cart *10/100)-cart,"rs")
        else:
            print("invalid user type)
else:
    if cart>= 2000:
        print("final amount= ",cart-(cart *5/100),"rs")
    else:
        print("final amount= ",cart)