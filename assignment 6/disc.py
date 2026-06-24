amt = int(input("enter purchase amount"))
if amt >=5000:
    print("final amount:",amt-amt*0.2)
elif amt >=2000 and amt <=5000:
    print("final amount:",amt-amt*10/100)
else: #amt < 2000:
    print("final amount:",amt-amt*5/100)

