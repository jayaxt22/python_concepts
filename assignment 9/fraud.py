amount = 70000
location = "international"
device = "new"
transactions = 4

if amount >= 50000:
    if location == "international":
        if device == "new":
            if transactions > 3:
                print("Risk Level = High Risk (Blocked)")
            else:
                print("Risk Level = Medium Risk")
        else:
            print("Risk Level = Medium Risk")

    else:
        if transactions > 5:
            print("Risk Level = Medium Risk")
        else:
            print("Risk Level = Low Risk")

else:
    unusual = "yes"

    if unusual == "yes":
        if device == "new":
            print("Risk Level = Medium Risk")
        else:
            print("Risk Level = Low Risk")
    else:
        print("Risk Level = Safe")