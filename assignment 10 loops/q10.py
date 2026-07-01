n = int(input("Enter a number: "))

count = 0
i = 1

while i <= n:
    if n % i == 0:
        count += 1
    i += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")