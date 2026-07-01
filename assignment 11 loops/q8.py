n = int(input("Enter a number: "))

largest = 0
smallest = 9

temp = n

while temp > 0:
    digit = temp % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    temp //= 10

s = largest + smallest

count = 0

for i in range(1, s + 1):
    if s % i == 0:
        count += 1

print("Largest =", largest)
print("Smallest =", smallest)
print("Sum =", s)

if count == 2:
    print("Prime")
else:
    print("Not Prime")