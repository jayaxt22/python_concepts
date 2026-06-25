"""
13. Number Range Display System (if-elif with loops)**
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using **if-elif-else and loops** to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same
"""

n1,n2=map(int,input("Enter The Two Number Sperated By Comma : ").split(","))

# by for loops
'''
if n1<n2:
    for i in range(n1,n2+1):
        print(i,end=" ")
elif n1>n2:
    for i in range(n1,n2-1,-1):
        print(i,end=" ")
else:
    print("both the numbers same") 
 '''
    
# by while loops
if n1<n2:
    while n1<n2:
        print(n1,end="->")
        n1+=1
    print(n2)
elif n1>n2:
    while n2<n1:
        print(n1,end="->")
        n1-=1
    print(n1)
else:
    print("both the numbers same") 