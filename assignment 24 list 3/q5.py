n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

found = False

for i in range(n):
    left_sum = 0
    right_sum = 0

    # Calculate left sum
    for j in range(i):
        left_sum += arr[j]

    # Calculate right sum
    for j in range(i + 1, n):
        right_sum += arr[j]

    if left_sum == right_sum:
        print("Equilibrium Index =", i)
        found = True
        break

if found == False:
    print("No Equilibrium Index Found")