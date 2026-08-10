# Extract prime IDs

n = int(input("Enter number of IDs: "))

ids = []

for i in range(n):
    value = int(input("Enter ID: "))
    ids.append(value)

prime_list = []

for number in ids:

    if number > 1:

        prime = True

        for i in range(2, number):

            if number % i == 0:
                prime = False
                break

        if prime:
            prime_list.append(number)

sum_prime = 0
count = len(prime_list)

if count == 0:
    max_prime = -1

else:
    max_prime = prime_list[0]

    for value in prime_list:

        sum_prime = sum_prime + value

        if value > max_prime:
            max_prime = value

print("Prime IDs =", prime_list)
print("Sum =", sum_prime)
print("Max =", max_prime)
print("Count =", count)