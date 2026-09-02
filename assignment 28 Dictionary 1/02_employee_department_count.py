# Q2. EMPLOYEE DEPARTMENT COUNT
# Count how many employees belong to each department and store
# the result in a dictionary.
# employees = ["HR","IT","HR","Sales","IT","IT","Finance"]
# Output: {'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}

# employees = ["HR", "IT", "HR", "Sales", "IT", "IT", "Finance"]

# Write your solution below
employees = list(input("Enter list : ").split(" "))
data = {}

for i in employees:
    if i in data:
        # Get Func Jaruri nhi hai hmesha 
        data[i]+=1
    else:
        data[i]=1

print(data)
