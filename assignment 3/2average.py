dist1= int(input("enter distance1 in km= "))
time1= int(input("enter time1 in hours= "))

dist2= int(input("enter distance2 in km= "))
time2= int(input("enter time2 in hours= "))
speed1= dist1//time1
speed2= dist2//time2
avg=(speed1+speed2)/2
print("average speed=",avg,"km/h")