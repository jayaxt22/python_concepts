#nested if else 
age = int(input("enter your age: "))
st = input("choose show time (morning/evening):")
dt = input("choose daytype(weekday/weekend)")
if age<=18:
    if st == "morning":
        print("ticket price= 100")
    else:    
        print("ticket price= 150")
else:
    if st =="evening":
        if dt == "weekend":
            print("ticket price= 300")
        else:
            print("ticket price= 250")
    else:
         print("ticket price= 150")
    
        