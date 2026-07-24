'''
Docstring for Assignment21 - Strings IV.a08
Find the Second Highest Repeating Character
Scenario

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input
aaabbbbccddeee
Output
e
Explanation
b → 4 times (highest)
e → 3 times (second highest)
Conditions
Program should work for both uppercase and lowercase letters.
Ignore spaces while counting.
If no second highest frequency exists, print:
Second highest repeating character not found
'''

n = input("Enter: ")

high = 0
second = 0

highC = ""
secondC = ""

visited = ""

for ch in n:
    if ch == " " or ch in visited:
        continue

    visited += ch

    count = 0

    for c in n:
        if ch == c:
            count += 1

    if count > high:
        second = high
        secondC = highC

        high = count
        highC = ch

    elif count >= second and count < high:
        second = count
        secondC = ch

if second == 0:
    print("Second highest repeating character not found")
else:
    print(secondC)