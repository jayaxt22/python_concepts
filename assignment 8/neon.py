n= int(input("enter a number= "))
temp=n 
sq=n*n
count=0
while sq>0:
    d= sq % 10
    count=count+d
    sq//=10 
  
if count==temp:    
    print("Glowing Success! You've found the Neon Number!") 
else:
    print("Try again! Not quite glowing yet.")