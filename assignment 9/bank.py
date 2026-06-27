amount=int(input("enter amount : "))
loq=input("enter location (domestic/international): ")
otp=input("enter verification status (verified/unverified): ")
age=int(input("enter account age:"))

if amount>=10000:
    if loq.lower()=="international":
        if otp.lower()=="verified":
            print("transaction status= allow")
        else:
            print("transaction status= block")
    elif loq.lower()=="domestic" :  
        if amount>=50000:
            if age>=2:
                print("transaction status: allow")
            else:
                print("transaction status: flagged ")
        else:
            print("transaction status: allow")
else:
     if otp.lower()=="verified":
        print("transaction status: allow")
     else:
        print("transaction status: flagged") 
         