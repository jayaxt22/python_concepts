salary = int(input("Enter salary: "))
rating = int(input("Enter rating (1-5): "))

if rating == 5:
    revised_salary = salary + salary * 0.25
elif rating == 4:
    revised_salary = salary + salary * 0.20
elif rating == 3:
    revised_salary = salary + salary * 0.10
elif rating == 2:
    revised_salary = salary + salary * 0.05
else:
    revised_salary = salary

if salary < 20000 and rating >= 4:
    revised_salary += 2000

print("Revised Salary:", revised_salary)