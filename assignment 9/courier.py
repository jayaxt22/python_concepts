pro=input("enter priority level (high/low): ")
stock=int(input("enter stock quantity: "))
distance=int(input("enter distance:"))
if stock>=100:
    if pro.lower()=="high":
        if distance<=200:
           print("dispatch status: immediately")
        else:
            print("dispatch status: dispatched via fast courier ")
    elif pro.lower()=="low":
        if stock>=300:
             print("dispatch status:bulk dispatch")
        else:
             print("normal dispatch")
elif stock>=50 :
     if pro.lower()=="high":
           print("stock status: partially dispatch")
     else:
           print("dispatch status: hold")
else:
    print("dispatch status: out of stock")