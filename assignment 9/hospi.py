age = 65
severity = "critical"
insurance = "yes"

if severity == "critical":
    if age >= 60:
        print("Treatment = Immediate ICU")
    else:
        print("Treatment = Emergency Ward")

elif severity == "moderate":
    if insurance == "yes":
        print("Treatment = Priority Treatment")
    else:
        print("Treatment = General Queue")

else:
    if age < 10:
        print("Treatment = Pediatric Priority")
    else:
        print("Treatment = Wait")