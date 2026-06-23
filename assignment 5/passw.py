#nested if else 
user = input("enter your username: ")
password = input("enter your password: ")
if user == "admin":
    if len(password) >= 8:
        print("valid user \nstrong password")
    else:
        print("valid User \nweak password")
else:
    print("invalid username and password")


