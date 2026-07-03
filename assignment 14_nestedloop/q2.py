'''
2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496
'''
a = int(input("enter first number:"))
b = int(input("enter second number:"))
while a<=b:
    n=a
    sum=0
    i=1
    while i<a:
        if a%i==0:
            sum+=i
        i+=1
    if sum == n:
        print(sum)
    
    a+=1 