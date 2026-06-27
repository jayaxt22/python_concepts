income = 45000
credit_score = 720
employment = "private"
debt = 10000

if income >= 50000:
    if credit_score >= 750:
        if debt < 20000:
            print("Card Type = Premium Card")
        else:
            print("Card Type = Gold Card")
    else:
        if employment == "government" and credit_score >= 650:
            print("Card Type = Gold Card")
        else:
            print("Card Type = Rejected")
else:
    if income >= 30000 and credit_score >= 700:
        print("Card Type = Silver Card")
    else:
        print("Card Type = Rejected")