class employee:
    def __init__(self,emp_id,emp_name,basic_salary,hra_percent,da_percent):
      
       self.emp_id=emp_id
       self.emp_name=emp_name
       self.basic_salary=basic_salary
       self.hra_percent=hra_percent
       self.da_percent=da_percent
       self.gross_salary=0
       self.hra=0
       self.da=0

    def calculate_hra(self):
        self.hra=self.basic_salary*self.hra_percent/100
        return self.hra


    def calculate_da(self):
        self.da=self.da_percent*self.basic_salary/100
        return self.da

    def calculate_gross_salary(self):
        self.gross_salary=self.basic_salary+self.hra+self.da
        return self.gross_salary


    def display_salary(self):
        print("=============== employee salary details ============")
        print("employee ID          :",self.emp_id)
        print("employee name        :",self.emp_name)
        print("employee basic salary:",self.basic_salary)
        print("employee hra         :",self.hra_percent,"%")
        print("emlpoyee da          :",self.da_percent,"%")
        print("employee gross salary:",self.gross_salary)
        print("====================== END =======================")

E1 = employee(12,"rahul",15000,12,4)

E1.calculate_hra()
E1.calculate_da()
E1.calculate_gross_salary()
E1.display_salary()
