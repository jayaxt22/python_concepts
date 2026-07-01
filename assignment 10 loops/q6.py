n = int(input("Enter a number: "))
square = n * n

temp = n
digits = 0

while temp > 0:
    digits += 1
    temp //= 10

power = 1
i = 0
while i < digits:
    power *= 10
    i += 1

if square % power == n:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")