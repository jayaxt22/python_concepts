marks = 38
attendance = 80
internal = 26

if marks >= 40:
    if attendance >= 75:
        if internal >= 20:
            print("Result = Pass")
        else:
            print("Result = Grace Pass")
    else:
        print("Result = Detained")

else:
    if marks >= 35 and internal >= 25:
        print("Result = Reappear")
    else:
        print("Result = Fail")