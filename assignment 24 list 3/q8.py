n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

found = False

for i in range(n):
    count = 0

    for j in range(n):
        if arr[i] == arr[j]:
            count += 1

    if count > n / 2:
        print("Majority Element =", arr[i])
        found = True
        break

if found == False:
    print("No Majority Element Found")
