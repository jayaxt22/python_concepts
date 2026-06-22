cart= int(input("enter cart value:"))
if cart >= 500:
    if cart >= 1200:
        print("free delivery applied.")
        print("10 % discount unlocked.")
    else:
        print("free delivery unlocked.")
else:
    print("add more items to unlock free delivery and discount.")        