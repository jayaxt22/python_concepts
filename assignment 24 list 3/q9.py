n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

happy = []

for num in arr:
    original = num
    seen = []

    while num != 1 and num not in seen:
        seen.append(num)

        sum_square = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            sum_square = sum_square + digit * digit
            temp = temp // 10

        num = sum_square

    if num == 1:
        happy.append(original)

print("Happy Numbers =", happy)
print("Count =", len(happy))

if len(happy) > 0:
    largest = happy[0]

    for i in range(1, len(happy)):
        if happy[i] > largest:
            largest = happy[i]

    print("Largest Happy Number =", largest)
else:
    print("Largest Happy Number = Not Available")