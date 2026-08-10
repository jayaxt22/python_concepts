n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

arr.sort()

longest = 1
current = 1

for i in range(1, n):
    if arr[i] == arr[i - 1] + 1:
        current += 1
    elif arr[i] != arr[i - 1]:
        current = 1

    if current > longest:
        longest = current

print("Longest Consecutive Length =", longest)