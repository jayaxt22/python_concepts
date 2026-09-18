class Student:

    def __init__(self, roll_number, student_name, marks1, marks2, marks3):
        self.roll_number = roll_number
        self.student_name = student_name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def calculate_total(self):
        return self.marks1+ self.marks2+self.marks3

    def calculate_percentage(self):
        return self.calculate_total()/3
    

    def calculate_grade(self):
        percent=self.calculate_percentage()

        if percent >=90:
            return "A"
        elif 75<=percent <=89:
            return "B"
        elif 60 <=percent <=74:
            return "C" 
        else:
            return "D"
        
    
    def display_result(self):
        print("------ Student Result ------")
        print("Roll Number      :", self.roll_number)
        print("Student Name     :", self.student_name)
        print("Total Marks      :", self.calculate_total())
        print("Percentage       :", round(self.calculate_percentage(), 2))
        print("Grade            :", self.calculate_grade())

roll_number = int(input("Enter Roll Number : "))
student_name = input("Enter Student Name : ")
marks1 = float(input("Enter Marks in Subject 1 : "))
marks2 = float(input("Enter Marks in Subject 2 : "))
marks3 = float(input("Enter Marks in Subject 3 : "))

student = Student(roll_number, student_name, marks1, marks2, marks3)
student.display_result()    