n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

for i in range(1, n + 2):
    found = False

    for j in range(n):
        if arr[j] == i:
            found = True
            break

    if found == False:
        print("Missing Number =", i)
        break