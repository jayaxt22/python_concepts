marks = int(input("Marks: "))
score = int(input("Entrance Score: "))
category = input("Category: ")

if marks >= 70:
    if score >= 80:
        if category == "general":
            print("Admission Status = Admitted")
        else:
            print("Admission Status = Admitted with Scholarship")
    else:
        if marks >= 85:
            print("Admission Status = Management Quota")
        else:
            print("Admission Status = Rejected")
else:
    if category != "general" and marks >= 60:
        if score >= 70:
            print("Admission Status = Waitlisted")
        else:
            print("Admission Status = Rejected")
    else:
        print("Admission Status = Rejected")