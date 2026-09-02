n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

duplicates = []

for i in range(n):
    count = 0

    for j in range(n):
        if arr[i] == arr[j]:
            count += 1

    if count > 1:
        if arr[i] not in duplicates:
            duplicates.append(arr[i])

duplicates.sort()

if len(duplicates) == 0:
    print("No Duplicate Numbers Found")
else:
    print("Duplicate Numbers =", duplicates)
    print("Count =", len(duplicates))