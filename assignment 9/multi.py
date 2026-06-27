experience = 6
rating = 4
projects = 2
salary = 45000

if experience >= 5:
    if rating >= 4:
        if projects >= 3:
            if salary <= 50000:
                print("Promotion Status = Promoted with 30% hike")
            else:
                print("Promotion Status = Promoted with 20% hike")
        else:
            print("Promotion Status = Promoted with 10% hike")
    else:
        print("Promotion Status = No Promotion")

else:
    if rating == 5:
        print("Promotion Status = Fast Track Promotion")
    else:
        print("Promotion Status = No Promotion")