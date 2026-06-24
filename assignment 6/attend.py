att = int(input("enter attendence:"))
if att >=75:
    print("Status: Eligible")
elif att >=60 and att <=74:
    print("Status: eligible with warning")
else:
    print("Status: not Eligible")