# Replace every number with its factorial

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter number: "))
    arr.append(value)

factorial_list = []

for number in arr:

    fact = 1

    for i in range(1, number + 1):
        fact = fact * i

    factorial_list.append(fact)

sum_fact = 0
even_count = 0
max_fact = factorial_list[0]

for value in factorial_list:

    sum_fact = sum_fact + value

    if value > max_fact:
        max_fact = value

    if value % 2 == 0:
        even_count = even_count + 1

print("Factorial List =", factorial_list)
print("Sum =", sum_fact)
print("Max =", max_fact)
print("Even Count =", even_count)