class rectangle:
    def __init__(self,length,breadth):

       self.length=length       
       self.breadth=breadth
    
       self.result=0
       self.result1=0

    def area(self):
        self.result=self.length*self.breadth
        return self.result


    def perimeter(self):
        self.result1=2*(self.length+self.breadth)
        return self.result1


    def display_salary(self):
        print("=============== rectangle details ============")
        print("length               :",self.length)
        print("breadth              :",self.breadth)
        print("area of rectangle    :",self.result)
        print("perimeter            :",self.result1)
        print("====================== END =======================")

E1 = rectangle(12,4)

E1.area()
E1.perimeter()
E1.display_salary()
