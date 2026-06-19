speed= int(input("enter speed= "))
hour,minute= map(int,input("enter time in hour and minutes = ").split(","))
time= minute/60+hour
dist= speed*time
print("time in hours=",time,"\n ditance=",dist,"km")