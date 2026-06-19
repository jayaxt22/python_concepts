p= int(input("enter principle amount= "))
r= int(input("enter rate of intererts= "))
t= int(input("enter time in years= "))
r=r/100
totalamount=p*(1+r)**t
ci=totalamount-p
print("amount= ",totalamount,"\ncompound interest=",ci)
