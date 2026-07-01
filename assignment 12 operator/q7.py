n = int(input("Enter number: "))

sum_alt = 0
position = 1

while n > 0:
    digit = n % 10

    if position % 2 == 1:
        sum_alt += digit

    position += 1
    n //= 10

count = 0

if sum_alt > 1:
    for i in range(1, sum_alt + 1):
        if sum_alt % i == 0:
            count += 1

print("Alternate Sum =", sum_alt)

if count == 2:
    print("Prime")
else:
    print("Not Prime")