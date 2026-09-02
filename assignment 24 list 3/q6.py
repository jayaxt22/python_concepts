n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

result = []

for i in range(n):
    product = 1

    for j in range(n):
        if i != j:
            product = product * arr[j]

    result.append(product)

print(result)