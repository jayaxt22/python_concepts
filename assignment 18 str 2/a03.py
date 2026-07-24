'''
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''

n=input("Enter The Employee : ")
a=n[:3]
b=n[3:]

if len(n)!=8:
    print("Length must be 8")

elif not (a=="EMP" or a=="emp") :
    print("not consider cause start")

elif not (b.isdigit()):
    print("not consider cause of digit")
else:
    print("Consider")
    
       
