amt = int(input("Enter bill amount: "))

if amt <= 1000:
    print("Final bill amount:", amt + amt * 0.05)
elif amt <= 5000:
    print("Final bill amount:", amt + amt * 0.12)
else:
    print("Final bill amount:", amt + amt * 0.18)
