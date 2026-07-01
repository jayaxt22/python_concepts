n = int(input("Enter a number: "))
temp = n
sum_fact = 0

while n > 0:
    digit = n % 10

    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1

    sum_fact += fact
    n //= 10

if sum_fact == temp:
    print("Strong Number")
else:
    print("Not Strong Number")