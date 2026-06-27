marks = 78
backlogs = 0
project = 85

if marks >= 75:
    if backlogs == 0:
        if project >= 80:
            print("Result = First Class with Distinction")
        else:
            print("Result = First Class")
    else:
        print("Result = First Class")

elif marks >= 60:
    if backlogs <= 2:
        print("Result = Second Class")
    else:
        print("Result = Pass Class")

elif marks >= 50:
    print("Result = Pass")

else:
    print("Result = Fail")