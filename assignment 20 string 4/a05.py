'''
Docstring for Assignment21 - Strings IV.a05
Find the Number of Unique Characters in a String
Scenario

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input
aabbccdde
Output
5

Explanation

Unique characters are:

a b c d e
'''

n=input("Enter The : ")
new=""

for i in n:
    if i not in new:
        new+=i
        # print(new)
# print(new)

print(len(new))
    