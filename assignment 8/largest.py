n= int(input("enter number= "))
big=0
while n>0:
    d=n%10
    if d>big:
        big=d
    n//=10    
    
print("largest digit=",big)  