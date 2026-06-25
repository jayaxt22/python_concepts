'''
Count Odd Digits**
A banking system flags IDs with too many odd digits for further verification.
Write a program to **count the number of odd digits in a given number using loops**.

Input: 123456
Output: Odd digits count = 3

'''

n=int(input("Enter The Number : "))
count=0

while n>0:
    d=n%10
    if d%2!=0:
        count+=1
    n//=10
   
print(f"Even Digits Count = {count}")