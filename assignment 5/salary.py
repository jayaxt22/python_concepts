salary = int(input("enter your salary: "))
if salary >= 30000:
    if salary >= 50000:
        print("PF applicable \nBonus applicable")
    else:
        print("PF applicable")
else:
    print("salary is low")