km = int(input("enter distance:"))
cat = input("enter class:")
cat= cat.lower()
if km <=100 :
     print("Total fare: 100$" if cat == "sleeper" else "Total fare:200$")
elif km >=101 and km <=500:
     print("Total fare: 300$" if cat == "sleeper" else "Total fare:600$")
else:
     print("Total fare: 500$" if cat == "sleeper" else "Total fare:  1000$")