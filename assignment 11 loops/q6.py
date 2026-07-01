n = int(input("Enter a number: "))

count = 0
smallest = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

for i in range(2, n):
    if n % i == 0:
        smallest = i
        break

if count > 2:
    print("Composite Number")
else:
    print("Not Composite Number")

print("Factors Count =", count)
print("Smallest Factor =", smallest)