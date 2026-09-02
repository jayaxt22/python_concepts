# Q5. WORD LENGTH GROUPING
# Group words according to their length and store the result in a dictionary.
#
# tags = ["python", "java", "api", "react", "html", "css"]
#
# Sample Output:
# {
#     3: ["api", "css"],
#     4: ["java", "html"],
#     5: ["react"],
#     6: ["python"]
# }
# Write your solution below

# tags = ["python", "java", "api", "react", "html", "css"]


tags = eval(input("Enter list : "))
ans = {}

for i in tags:
    length = len(i)
    if length in ans:
        ans[length].append(i)
    else:
        ans[length]=[i]

ans=dict(sorted(ans.items()))
print(ans)