n = int(input("Enter number: "))

sum_factors = 0

for i in range(1, n):
    if n % i == 0:
        sum_factors += i

else:
    if sum_factors == n:
        print("Reward Unlocked")
    else:
        print("Try Again")