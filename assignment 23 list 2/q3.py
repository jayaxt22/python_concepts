# Find peak energy values

n = int(input("Enter number of energy readings: "))

energy = []

for i in range(n):
    value = int(input("Enter energy value: "))
    energy.append(value)

peaks = []

if n == 1:
    peaks.append(energy[0])

else:
    for i in range(n):

        if i == 0:
            if energy[i] >= energy[i + 1]:
                peaks.append(energy[i])

        elif i == n - 1:
            if energy[i] >= energy[i - 1]:
                peaks.append(energy[i])

        else:
            if energy[i] >= energy[i - 1] and energy[i] >= energy[i + 1]:
                peaks.append(energy[i])

if len(peaks) == 0:
    print(-1)

else:

    sum_square = 0
    total = 0

    max_peak = peaks[0]
    min_peak = peaks[0]

    for value in peaks:

        sum_square = sum_square + value * value
        total = total + value

        if value > max_peak:
            max_peak = value

        if value < min_peak:
            min_peak = value

    average = total / len(peaks)
    difference = max_peak - min_peak

    print("Peaks =", peaks)
    print("Sum of Squares =", sum_square)
    print("Average =", average)
    print("Difference =", difference)