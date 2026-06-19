seconds = int(input("enter the event value in seconds"))
hours = seconds//3600
minutes= (seconds%3600)//60
second = seconds%60
print("hours:",hours," minutes:", minutes," seconds:",second) 
