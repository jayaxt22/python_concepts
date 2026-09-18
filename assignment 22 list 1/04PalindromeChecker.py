"""
4.
Palindrome Number List Checker
Scenario
A system checks lucky numbers which are palindromes.
Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases
Input:
[121, 131, 20, 44, 55, 100]
Output:
Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
"""
numbers=[]
number=input("enter the number with space between them:").split()
numbers.extend(map(int,number))


palindrome=[]

pcount=0


for num in numbers:
    temp=num
    sum=0
    while num>0:
         rev=num%10
         sum=sum*10+rev
         num//=10 

    if sum==temp:
         palindrome.append(sum)  
         pcount+=1 
     
print("palindromes:",palindrome)
print("count:",pcount)
largest=max(palindrome)
print("largest:",largest)
palindrome.sort()
print("sorted:",palindrome)