'''
Docstring for a05
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code

'''
n=input("Enter The product code : ")

r=n[::-1]
print(r)

if r==n:
    print("Palindrome")
else:
    print("not palindrome")