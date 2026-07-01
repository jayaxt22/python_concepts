n = int(input("Enter current ID: "))

num = n + 1

while True:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Next Prime ID =", num)
        print("Gap =", num - n)
        break

    num += 1