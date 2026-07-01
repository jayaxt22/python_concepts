n = int(input("Enter a number: "))

even = 0
odd = 0

temp = n

while temp > 0:
    digit = temp % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    temp //= 10

diff = abs(even - odd)

count = 0

if diff > 1:
    for i in range(1, diff + 1):
        if diff % i == 0:
            count += 1

print("Even Count =", even)
print("Odd Count =", odd)
print("Difference =", diff)

if count == 2:
    print("Prime")
else:
    print("Not Prime")