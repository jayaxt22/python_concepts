n = input("Enter number: ")

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] == n[j]:
            print("Invalid Code")
            break
    else:
        continue
    break
else:
    print("Valid Unique Code")