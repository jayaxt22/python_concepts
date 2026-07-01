n = int(input("Enter a number: "))
temp = n
sum_digits = 0

while n > 0:
    sum_digits += n % 10
    n //= 10

if temp % sum_digits == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")