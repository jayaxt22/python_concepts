age = int(input("Policy Age: "))
claim = int(input("Claim Amount: "))
accident = input("Accident Type: ")

if age >= 2:
    if claim <= 50000:
        if accident == "minor":
            print("Claim Status = Approved")
        else:
            print("Claim Status = Approved with Inspection")
    elif claim <= 200000:
        if accident == "major":
            print("Claim Status = Approved with Investigation")
        else:
            print("Claim Status = Rejected")
    else:
        print("Claim Status = Rejected")
else:
    if accident == "minor":
        print("Claim Status = Rejected")
    else:
        print("Claim Status = Pending Review")