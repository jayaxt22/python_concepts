n = int(input("Enter a number: "))

temp = n
zero_count = 0
sum_digits = 0
smallest = 9

while temp > 0:
    digit = temp % 10

    if digit == 0:
        zero_count += 1

    sum_digits += digit

    if digit < smallest:
        smallest = digit

    temp //= 10

final_result = (zero_count + sum_digits) * smallest

count = 0

if final_result > 1:
    for i in range(1, final_result + 1):
        if final_result % i == 0:
            count += 1

print("Zero Count =", zero_count)
print("Sum =", sum_digits)
print("Smallest Digit =", smallest)
print("Final Result =", final_result)

if count == 2:
    print("Prime")
else:
    print("Not Prime")