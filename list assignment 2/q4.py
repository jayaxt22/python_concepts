# Sum of leaders after removing negative numbers and zero

n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    value = int(input("Enter number: "))
    arr.append(value)

positive = []

for value in arr:
    if value > 0:
        positive.append(value)

if len(positive) == 0:
    print(-1)

else:

    leaders = []

    largest = positive[len(positive) - 1]
    leaders.append(largest)

    for i in range(len(positive) - 2, -1, -1):

        if positive[i] > largest:
            leaders.append(positive[i])
            largest = positive[i]

    sum_leaders = 0

    for value in leaders:
        sum_leaders = sum_leaders + value

    print("Filtered Array =", positive)
    print("Leaders =", leaders)
    print("Sum of Leaders =", sum_leaders)