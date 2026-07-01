n = input("Enter number: ")

for i in range(len(n) - 1):
    if int(n[i + 1]) <= int(n[i]):
        print("Unstable Number")
        break
else:
    print("Stable Number")