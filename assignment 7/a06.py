'''

Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to **check whether a number is an Armstrong number using loops**.

Input: 153
Output: Armstrong
'''

n=int(input("Enter The Number : "))
n1=n
count=0
sum=0
p=1

while n>0:
    count+=1
    n//=10

n=n1

while n>0:
    d=n%10
    for i in range(1,count+1):
        p*=(d)
    sum+=p
    n//=10
    p=1
  
if n1==sum:
    print("Armstrong")
else:
    print("No Armstrong")
    
    


