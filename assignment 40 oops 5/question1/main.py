from models.employee import Employee,Developer,Manager
from rich.prompt import Prompt


emp_id=int(input("Enter ID : "))
emp_name=input("Enter Name : ")
emp_salary=int(input("Enter Salary : "))

print("Choose the Role")
print("1.Developer")
print("2.Manager")

choice=Prompt.ask(
    "Enter Your Choice",
    choices=["1","2"]
)


if choice=="1":
    # print("Developer")
    program_lang=input("Enter Program Language : ")
    d1=Developer(emp_id,emp_name,emp_salary,program_lang)
    d1.display_details()
    d1.write_code()
else:
    # print("Manager")
    team_size=int(input("enter the team size:"))
    m1=Manager(emp_id,emp_name,emp_salary,team_size)
    m1.display_details()
    m1.manage_team()

