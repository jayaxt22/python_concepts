data = float(input("enter daily data ussagein Gb:"))
if data >3.0:
    print("recommended plan: premium plan")
elif data >=1.0 and data <=3.0:
    print("recommend plan: standard plan")
else:
    print("recommended plan: basic plan")