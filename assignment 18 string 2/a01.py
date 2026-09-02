'''
Docstring for a01
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''

n=input("Enter UserName : ")

if len(n) < 5 or len(n) > 12:
    print("Length must be between 5 and 12")

elif not n[0].isalpha():
    print("Username must start with a letter")

elif " " in n:
    print("Username must not contain spaces")

else:
    valid = True

    for ch in n:
        if not (ch.isalpha() or ch.isdigit() or ch == "_"):
            valid = False
            break

    if valid:
        print("Valid Username")
    else:
        print("Username can contain only letters, digits, and underscore (_)")

            

    