# Q8. LIBRARY BOOK ISSUE TRACKER
# Count how many times each book was issued.
# books = ["Python","Java","Python","C++","Java","Python"]

# books = ["Python", "Java", "Python", "C++", "Java", "Python"]
# Sample Output:
# {
# 'Python':3,
# 'Java':2,
# 'C++':1
# }

# Write your solution below

books = eval(input("Enter list : "))
ans = {}

for i in books:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=1
print(ans)