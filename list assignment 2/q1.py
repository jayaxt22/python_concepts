#peak element finder

n = int(input("Enter number of checkpoints: "))

elevation = []

for i in range(n):
    value = int(input("Enter elevation: "))
    elevation.append(value)

peak_index = -1

if n == 1:
    peak_index = 0
else:
    for i in range(n):

        if i == 0:
            if elevation[i] >= elevation[i + 1]:
                peak_index = i
                break

        elif i == n - 1:
            if elevation[i] >= elevation[i - 1]:
                peak_index = i
                break

        else:
            if elevation[i] >= elevation[i - 1] and elevation[i] >= elevation[i + 1]:
                peak_index = i
                break

print("Peak Index =", peak_index)