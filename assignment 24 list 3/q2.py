n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

found = False

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print("First Repeating Number =", arr[i])
            found = True
            break

    if found == True:
        break

if found == False:
    print("No Repeating Number Found")