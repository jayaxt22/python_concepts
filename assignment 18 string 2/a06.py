'''
Docstring for a06
Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''

first=input("enter the first product code :  ").lower()
second=input("enter the second product code : ").lower()

ignSpace=second.replace(" ","")
print(ignSpace)


if sorted(first)==sorted(ignSpace):
    print("match")
else:
    print("not match ")

