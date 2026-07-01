n = int(input("Enter number: "))

temp = n
sum_digits = 0

while temp > 0:
    sum_digits += temp % 10
    temp //= 10

temp = n
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

diff = abs(n - rev)

final_result = sum_digits + diff

count = 0
for i in range(1, final_result + 1):
    if final_result % i == 0:
        count += 1

print("Sum of Digits =", sum_digits)
print("Reverse =", rev)
print("Difference =", diff)
print("Final Result =", final_result)

if count == 2:
    print("Prime")
else:
    print("Not Prime")