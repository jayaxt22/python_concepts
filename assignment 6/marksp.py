marks =int(input("enter units: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75 and marks <=89:
    print("Grade: B")
elif marks >= 60 and marks<=74:
    print("Grade : C")
elif marks >= 50 and marks<=59:
    print("Grade : D")
else:
    print("Fail")