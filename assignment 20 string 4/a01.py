'''
Docstring for Assignment21 - Strings IV.a01

Remove All Special Characters from a String
Scenario

Online Banking Customer Data Cleaning System

A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.

Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

Alphabets (A–Z, a–z)
Numbers (0–9)
Spaces

Store the cleaned value back into the original string variable.

Example 1

Input

Deepika@@ Padukone!! 123

Output

Deepika Padukone 123
Example 2

Input

Ajay###Singh$$$

Output

AjaySingh
'''

n=input("Enter : ")
s=""
for i in range(len(n)):
    if n[i] not in "!@#$%^&*-_":
        s += n[i]

print(s)