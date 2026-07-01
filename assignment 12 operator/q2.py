n = int(input("Enter number: "))

temp = n
sum_digits = 0
product = 1

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    product *= digit
    temp //= 10

diff = product - sum_digits

temp = abs(diff)
digits = 0

if temp == 0:
    digits = 1
else:
    while temp > 0:
        digits += 1
        temp //= 10

final_result = diff + digits

count = 0
for i in range(1, final_result + 1):
    if final_result % i == 0:
        count += 1

print("Sum =", sum_digits)
print("Product =", product)
print("Difference =", diff)
print("Digits =", digits)
print("Final Result =", final_result)

if count == 2:
    print("Prime")
else:
    print("Not Prime")