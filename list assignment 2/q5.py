

n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    value = int(input("Enter number: "))
    arr.append(value)

result = []

for value in arr:
    if value >= 0:
        result.append(value)

for value in arr:
    if value < 0:
        result.append(value)

print("Result Array =")

for value in result:
    print(value, end=" ")