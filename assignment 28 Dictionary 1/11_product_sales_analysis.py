# Q11. PRODUCT SALES ANALYSIS
# Count sales of each product and display products in sorted order.
# sales = ["Mobile","Laptop","Mobile","Tablet","Laptop","Mobile"]

sales = ["Mobile", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile"]
# Sample Output:
# Laptop : 2
# Mobile : 3
# Tablet : 1

# Write your solution below

# emails = eval(input("Enter list : "))
ans = {}

for i in sales:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=1

ans=dict(sorted(ans.items()))
for k,v in ans.items():
    print(k," : ",v)