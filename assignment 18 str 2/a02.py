'''
Docstring for a02
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12
'''

n=input("Enter The Number : ")
count=0

if n.isalpha():
    print("please enter the number only ")
else:
    for ch in n:
        
        if ch.isdigit():
            # print(ch)
            count+=1
        

print(f'Total Digits : {count}')
