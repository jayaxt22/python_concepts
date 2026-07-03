'''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    n = a
    p=len(str(n))
    sum = 0
   

    while n>0:
          digit=n%10
          sum=sum+digit**p
          n//=10
        

    if sum == a:
        print(a)

    a += 1