'''
Docstring for a02
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST
'''
n=input("Enter The Name : ")
s=""
for i in range(len(n)):
    if i==0 or n[i-1]==" ":
        if 'a'<=n[i]<='z' :
            s+=chr(ord(n[i])-32)
        elif 'A'<=n[i]<='Z':
            s+=n[i]
        

print(s)
