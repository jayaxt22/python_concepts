mos=int(input("enter soil moisture: "))
crop=input("enter crop type: ")
temp=int(input("enter temperature:"))
rain=input("enter rainfall status(yes/no): ")

if mos<=30:
    if temp<=35:
      if crop.lower()=="wheat":
          print("irrigation: high water supply")
      else:
          print("irrigation: moderate water supply")
    else:
          print("irrigation: moderate water supply")
elif mos<=60:
      if rain.lower()=="yes":
          print("irrigation: delay")
      else:
          print("irrigation: light irrigation")
else:         
    print("irrigation: No")