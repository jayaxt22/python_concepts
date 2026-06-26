n= int(input("enter number= "))
count=0
while n>0:
    d=n%10
    if d%2!=0:
        count+=1
    n=n//10    
print("number of odd digits:",count)