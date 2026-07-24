n=input("Enter Vehicle Number : ").lower()
print(len(n))
print(n.count(" "))
print( n[:2], n[2:4],n[4:6],n[6:])
if  n.count(" ")==0 and len(n)==10:
    a=n[:2]
    b=n[2:4]
    c=n[4:6]
    d=n[6:]
    if  a.isalpha() and c.isalpha and b.isdigit() and d.isdigit():
         print(" valid")
    
    else:
         print("not valid")
else:
     print("Not valid  ")
