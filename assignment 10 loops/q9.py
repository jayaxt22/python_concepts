n = input("Enter a number: ")

sum_diff = 0
largest = 0

print("Step Differences:", end=" ")

for i in range(len(n) - 1):
    d1 = int(n[i])
    d2 = int(n[i + 1])

    diff = abs(d1 - d2)

    print(diff, end=" ")

    sum_diff += diff

    if diff > largest:
        largest = diff

print()
print("Sum =", sum_diff)
print("Largest =", largest)

if sum_diff % len(n) == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")