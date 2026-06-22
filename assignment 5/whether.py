temp = int(input("enter your temperature :"))
hum = int(input("enter humidity= "))
if temp >= 30:
    print("hot day")
    if hum >= 70:
         print("high humidity alert")
    else:
         print("humidity is normal")
else:
    print("normal day")
       
          

