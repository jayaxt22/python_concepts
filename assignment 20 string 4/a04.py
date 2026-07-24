'''
Docstring for Assignment21 - Strings IV.a04
Find the Shortest Word in a Sentence
Scenario

Telecom SMS Cost Optimization System

A telecom company charges customers based on the length of words used in bulk SMS campaigns.

The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.

Input
Python is very easy to learn
Output
is
'''

n = input("Enter: ")

shortest = ""
first = True

for word in n.split():
    if first:
        shortest = word
        first = False
    elif len(word) < len(shortest):
        shortest = word

print(shortest)
    
