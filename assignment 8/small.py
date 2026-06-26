n= int(input("enter number= "))
big=10
while n>0:
    d=n%10
    if d<big:
        big=d
    n//=10    
    
print("smallest digit=",big) 