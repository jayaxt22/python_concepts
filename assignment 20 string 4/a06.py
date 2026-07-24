'''
Docstring for Assignment21 - Strings IV.a06
Find Occurrence of a Word in a String
Scenario

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence
iphone is good and iphone battery is strong
Word
iphone
Output
2
'''

n=input("Enter The  : ")

word=input("Enter The : ")

count=0

for w in n.split():
    if w==word:
        count+=1
    
print(count)