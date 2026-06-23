#nested if else 
age = int(input("enter your age: "))
weight = float(input("enter your weight in kg"))
goal = input("enter your goal(weight loss/muscle gain): ")
goal = goal.lower()
if age >= 18:
    if weight >= 80:
        if goal == "weight loss":
            print("plan= cardio plan")
        else:
            if goal == "muscle gain":
               print("plan = strength plan")
            else:
                print("enter valid goal")
    else:
        print("general fitness plan")
else:
    print("not allowed")

