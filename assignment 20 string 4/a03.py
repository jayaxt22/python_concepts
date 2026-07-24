'''
Docstring for Assignment21 - Strings IV.a03
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:

```
e
```
'''

n=input("Enter The input : ")

for i in range(len(n)):
    count = 0

    for j in range(len(n)):
        if n[i] == n[j]:
            count += 1

    if count == 1:
        print(n[i])
        break

