'''
Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to **reverse a given integer using loops**.

Input: 1234
Output: 4321

'''
n=int(input("Enter The Number : "))

rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
    
print(f"reverser will be :{rev}")