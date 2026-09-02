# Q1. ONLINE SHOPPING CART
# Write a program to accept a dictionary from the user and calculate
# the total quantity of products purchased.
# Sample: {"Laptop":2,"Mouse":3,"Keyboard":1}
# Output: Total Quantity = 6

data = input("Enter product dictionary: ")
products = eval(data)

# Write your solution below

count=0

for i in products.values():
    count+=i
print("Total Quantity = ",count)