"""
2.Employee Salary Processing
Store employee salaries in a List and calculate details.
Requirements:
Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000
Test Cases:
Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
"""
salary=[]
n=int(input("enter the length of list:"))
for i in range(n):
    salry=int(input("enter salary:"))
    salary.append(salry)

total=0
print(salary)
for salaries in range(len(salary)):
    total+=salary[salaries]

avg=total/len(salary)
print("Average salary:",avg)

high=[]
for sal in salary:
    if sal>=avg:
        high.append(sal)

print("salary greater than averageL:",high)
for sal in salary.copy():
    if sal<=15000:
        salary.remove(sal)
print("salary removed lessthan 15000")
print(salary)
