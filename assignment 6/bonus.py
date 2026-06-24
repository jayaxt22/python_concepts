amt = int(input("enter salary:"))
years= int(input("enter years of experience:"))
if years >10:
    print("bonus amount:",amt*0.2)
elif years >=5 and years <=10:
    print("bonus amount:",amt*10/100)
elif years >=2 and years <5 :
    print("bonus amount:",amt*5/100)
else:
    print("NO bonus")

