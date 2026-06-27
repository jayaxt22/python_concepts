age = 23
bmi = 22
running_time = 14
medical = "fit"

if 18 <= age <= 25:
    if 18 <= bmi <= 25:
        if running_time <= 15:
            if medical == "fit":
                print("Selection Status = Selected")
            else:
                print("Selection Status = Medical Reject")
        else:
            print("Selection Status = Physical Fail")
    else:
        print("Selection Status = BMI Fail")

elif 26 <= age <= 30:
    if running_time <= 14 and medical == "fit":
        print("Selection Status = Conditional Selection")
    else:
        print("Selection Status = Rejected")

else:
    print("Selection Status = Not Eligible")