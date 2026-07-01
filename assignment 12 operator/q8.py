amount = int(input("Enter amount: "))

count = 0

while amount >= 100:
    count += 1
    amount -= 100

print("Notes =", count)