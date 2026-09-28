class Employee:

    def __init__(self,emp_id,emp_name,salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.salary=salary #as setter


    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):

        if value>0:
              self.__salary=value
        else:
             print('invalid Value')

    @salary.deleter
    def salary(self):
         del self.__salary

    
    def display_details(self):
        print(f"Dsiplay Details")
        print(f"Employee Id :{self.emp_id}")
        print(f"Employee Name :{self.emp_name}")
        print(f"Salary :{self.salary}")

    
    

class Developer(Employee):
    def __init__(self,emp_id,emp_name,salary,program_lang):
        self.program_lang=program_lang
        super().__init__(emp_id,emp_name,salary)

    def write_code(self):
         print(f"{self.emp_name} is developing by {self.program_lang}")

        

    def display_details(self):
        super().display_details()
        print(f"Role : developer")
        print(f"Language : {self.program_lang}")


class Manager(Employee):
    def __init__(self,emp_id,emp_name,salary,team_size):
            self.team_size=team_size
            super().__init__(emp_id,emp_name,salary)

    def manage_team(self):
         print(f"{self.emp_name} is managing team of size {self.team_size}")

    def display_details(self):
            super().display_details()
            print(f"Role : Manager")
            print(f"Team Size : {self.team_size}")