# Q7. ONLINE EXAM RESULT SYSTEM
# Display names of students who passed.
# Passing Marks = 50
# results = {"Ajay":88,"Ravi":45,"Neha":76,"Aman":39}

# results = {
#     "Ajay": 88,
#     "Ravi": 45,
#     "Neha": 76,
#     "Aman": 39
# }
# Sample Output:
# Ajay
# Neha
# Write your solution below

results = eval(input("Enter list : "))
ans = {}

for i,v in results.items():
    if v>=50:
        ans[i]=v

for i in ans:
    print(i)