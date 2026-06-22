age= int(input("enter age"))
id= input("do you have id proof? (yes/no) ")
id= id.lower()  
if age >= 18:
    print("you are eligible to vote.")
    if id=="yes":
        print("welcome to booth")

    else:
        print("not allowed to vote without id proof")
else:
    print("you are not eligible to vote.")        