age = int(input("enter your age= "))
bmi = int(input("enter your bmi= "))
if age >= 18:
    print("gym access granted")
    if bmi>25:
        print("enroll in weight loss program")
    else:
        print("enroll in muscle gain program")
else:
    print("not eligible for gym")