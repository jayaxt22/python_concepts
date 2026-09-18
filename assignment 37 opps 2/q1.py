class Employee:

    def __init__(self, employee_id, employee_name, basic_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.15

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display_details(self):
        print("------ Employee Salary Details ------")
        print("Employee ID      :", self.employee_id)
        print("Employee Name    :", self.employee_name)
        print("Basic Salary     :", self.basic_salary)
        print("HRA              :", self.calculate_hra())
        print("DA               :", self.calculate_da())
        print("Gross Salary     :", self.calculate_gross_salary())


employee_id = input("Enter Employee ID : ")
employee_name = input("Enter Employee Name : ")
basic_salary = float(input("Enter Basic Salary : "))

employee = Employee(employee_id, employee_name, basic_salary)
employee.display_details()