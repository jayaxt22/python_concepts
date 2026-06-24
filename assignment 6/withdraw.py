amt = int(input("enter account balance:"))
if amt <1000:
    print("no withdrawel allowed")
elif amt >=1000 and amt <=5000:
    print("Maximum withdrawal: ₹1000")
elif amt >5000 :
    print("Maximum withdrawal: ₹5000")
