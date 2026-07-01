'''
Docstring for a02
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
'''
n1=int(input("Enter The 1st Number: "))
n2=int(input("Enter The 2st Number: "))

count=0

while n1<=n2:
    if n1%7==0:
        count+=1
    n1+=1

print(count)