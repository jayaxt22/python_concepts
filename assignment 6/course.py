course = input("Enter course category: ")
user = input("Enter user type: ")

if course == "Programming":
    fee = 5000
elif course == "Design":
    fee = 4000
else:
    fee = 3000

if user == "Student":
    fee = fee - fee * 20 / 100
elif user == "Working Professional":
    fee = fee - fee * 10 / 100

print("Final Course Fee:", fee)