n = int(input("Enter a number: "))
temp = n
duck = False

while n > 0:
    digit = n % 10

    if digit == 0:
        duck = True

    n //= 10

if duck:
    print("Duck Number")
else:
    print("Not Duck Number")