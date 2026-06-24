inc = int(input("enter annual income"))
if inc <=250000:
    print("not TAX payable")
elif inc >=250001 and inc <=500000:
    print("TAX payable:",inc*5/100)
elif inc >=500001 and inc <=1000000:
    print("TAX payable:",inc*20/100)
else:
    print("TAX payable:",inc*30/100)
