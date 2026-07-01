n = int(input("Enter a number: "))

sum_digits = 0
temp = n

while temp > 0:
    sum_digits += temp % 10
    temp //= 10

count = 0

for i in range(1, sum_digits + 1):
    if sum_digits % i == 0:
        count += 1

print("Sum =", sum_digits)

if count == 2:
    print("Lucky Number")
else:
    print("Normal Number")