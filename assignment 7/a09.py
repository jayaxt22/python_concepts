'''

Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''

n=int(input("Enter The Number : "))
sum=0
isOdd=False

while n>0:
    d=n%10
    if d%2==1:
        isOdd=True
    else:
        isOddd=False
        
    n//=10
        
   
print("Not All Even" if isOdd else "All Even")