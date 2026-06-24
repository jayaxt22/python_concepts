temp = int(input("enter temperature in celcius:"))
if temp <0:
    print("Weather Condition: Freezing")
elif temp >=0 and temp <=20:
    print("Weather Condition: cold")
elif temp >=21 and temp <=35:
    print("Weather Condition: Warm")
else:
    print("Weather Condition: Hot")