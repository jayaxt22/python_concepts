demand=int(input("enter demand: "))
time=input("enter location (normal/peak): ")
dist=int(input("enter distance:"))

if demand>=80:
    if time.lower()=="peak":
        if dist>=10:
            print("fare Multiplier= 2x fare")
        else:
            print("fare Multiplier= 1.5x fare")
    elif time.lower()=="normal" :  
        if demand>=90:
                print("fare Multiplier= 1.8x fare")
        else:
                print("fare Multiplier= 1.3x fare ")
elif demand>=50:
      if time.lower()=="peak":
            print("fare Multiplier= 1.2x fare")
      elif time.lower()=="normal" :
            print("fare Multiplier= normal fare")
      else:
          print("invalid time")
else:
    print("fare multiplier= normal fare")
         