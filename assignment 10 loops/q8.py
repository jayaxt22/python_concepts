n = int(input("Enter transaction ID: "))

rev = 0
temp = n

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

diff = abs(n - rev)

count = 0
temp = diff

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print("Reverse =", rev)
print("Difference =", diff)
print("Digits =", count)

if diff == 0:
    print("Perfect Match")
elif diff % 9 == 0:
    print("Verified")
else:
    print("Rejected")