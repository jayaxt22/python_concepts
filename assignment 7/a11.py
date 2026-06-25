'''
Count Occurrence of a Digit**
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to **count how many times a given digit appears in a number using loops**.

Input: Number = 122312, Digit = 2
Output: 3

'''

n,d=map(int,input("Enter The Number and Digit  : ").split(","))
count=0

while n>0:
    d1=n%10
    if d1==d:
        count+=1
    n//=10
   
print(f"Occurrence Of A Digit = {count}")