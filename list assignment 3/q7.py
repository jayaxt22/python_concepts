n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

k = int(input("Enter K: "))

for i in range(k):
    last = arr[n - 1]

    for j in range(n - 1, 0, -1):
        arr[j] = arr[j - 1]

    arr[0] = last

print(arr)