# Q10. EMAIL DOMAIN COUNTER
# Count users belonging to each email domain.
# Example domains: gmail.com, yahoo.com, outlook.com

# emails = [
#     "ajay@gmail.com",
#     "ravi@yahoo.com",
#     "neha@gmail.com",
#     "aman@outlook.com",
#     "abc@gmail.com"
# ]

# Sample Output:
# {
# 'gmail.com':3,
# 'yahoo.com':1,
# 'outlook.com':1
# }

# Write your solution below
emails = eval(input("Enter list : "))
ans = {}

for i in emails:
    domain = i.split("@")[1] 
    if domain in ans:
        ans[domain]+=1
    else:
        ans[domain]=1


print(ans)