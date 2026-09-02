# Q12. ONLINE FOOD DELIVERY ANALYSIS
# Count orders of each food item and find the most ordered item.
# orders = ["Pizza","Burger","Pizza","Pasta","Burger","Pizza","Pasta"]

orders = ["Pizza", "Burger", "Pizza", "Pasta","Pasta","Pasta", "Burger", "Pizza", "Pasta"]
# Sample Output:
# Pizza : 3
# Burger : 2
# Pasta : 2

# Most Ordered : Pizza

# Write your solution below
ans = {}

for i in orders:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=1

ans=dict(sorted(ans.items()))
most_ordered_item=""
most_ordered=0
for k,v in ans.items():
    if v>most_ordered:
        most_ordered_item=k
        most_ordered=v
    print(k," : ",v)
print("Most Ordered : ",most_ordered_item)