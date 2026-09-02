# Find all peak traffic values

n = int(input("Enter number of traffic readings: "))

traffic = []

for i in range(n):
    value = int(input("Enter traffic value: "))
    traffic.append(value)

peaks = []

if n == 1:
    peaks.append(traffic[0])

else:
    for i in range(n):

        if i == 0:
            if traffic[i] >= traffic[i + 1]:
                peaks.append(traffic[i])

        elif i == n - 1:
            if traffic[i] >= traffic[i - 1]:
                peaks.append(traffic[i])

        else:
            if traffic[i] >= traffic[i - 1] and traffic[i] >= traffic[i + 1]:
                peaks.append(traffic[i])

sum_peaks = 0
product = 1
max_peak = peaks[0]

for value in peaks:
    sum_peaks = sum_peaks + value
    product = product * value

    if value > max_peak:
        max_peak = value

print("Peaks =", peaks)
print("Sum =", sum_peaks)
print("Product =", product)
print("Max Peak =", max_peak)