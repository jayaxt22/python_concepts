class student:
    total_marks=300
    obtained_marks=0
    def __init__(self,name,rollno,emarks,smarks,mmarks):
        self.name=name
        self.rollno=rollno
        self.emarks=emarks
        self.smarks=smarks
        self.mmarks=mmarks
        self.obtained_marks=0

    def calculate_total(self):

        self.obtained_marks=self.mmarks+self.smarks+self.emarks
        return self.obtained_marks



    def calculate_percentage(self):
        percent=(self.obtained_marks/self.total_marks)*100
        return percent
        

    def display_result(self):
        print("Student Name:", self.name,"\nRoll Number:",self.rollno,
        "\nTotal Marks:", self.calculate_percentage(),"\nPercentage:", self.calculate_percentage(),"%") 

name=input("enter the name:")
rollno=int(input("enter the roll no:"))
smarks=int(input("enter the marks in science:"))
mmarks=int(input("enter the marks in maths:"))
emarks=int(input("enter the marks in english:"))

s1= student(name,rollno,emarks,smarks,mmarks)
s1.calculate_total()
s1.calculate_percentage()
s1.display_result()