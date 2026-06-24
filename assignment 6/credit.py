salary = int(input("Salary: "))
credit = int(input("Credit Score: "))
loans = int(input("Existing Loans: "))

if salary >= 30000:
    if credit >= 750:
        if loans == 0:
            print("Risk Level = Low Risk")
        elif loans <= 2:
            print("Risk Level = Medium Risk")
        else:
            print("Risk Level = High Risk")
    else:
        if salary >= 50000:
            if credit >= 650:
                print("Risk Level = Medium Risk")
            else:
                print("Risk Level = High Risk")
        else:
            print("Risk Level = High Risk")
else:
    print("Risk Level = Not Eligible")