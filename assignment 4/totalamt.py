principle= int(input("enter principal amount= "))
rate= int(input("enter rate= "))
time= int(input("enter time= "))
rate= rate/100
pp= principle*(1+rate)**time 
print("amount with interest=",pp,"rs") 