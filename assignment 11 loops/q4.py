n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime Number")

    num = n + 1

    while True:
        c = 0

        for i in range(1, num + 1):
            if num % i == 0:
                c += 1

        if c == 2:
            print("Next Prime =", num)
            break

        num += 1

else:
    print("Not Prime Number")

    num = n - 1

    while num > 1:
        c = 0

        for i in range(1, num + 1):
            if num % i == 0:
                c += 1

        if c == 2:
            print("Previous Prime =", num)
            break

        num -= 1