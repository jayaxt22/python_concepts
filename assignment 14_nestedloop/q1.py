'''
1.
Multiplication Table Generator

Scenario:
A school learning app helps students practice multiplication tables.
The user enters a number n, and the system prints multiplication tables from 1 to n using nested loops.

Input:
Enter limit: 3

Output:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9

'''
a = int(input("enter first number:"))
b = int(input("enter second number:"))
while a<=b:
    n=a
    i=1
    while i<=10:
        print(n,"x",i,"=",n*i)
        i+=1
    print()    
    a+=1