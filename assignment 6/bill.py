unit= int(input("enter units: "))
if unit <=100:
    bill= unit*5
elif unit <=200:
    bill= (100*5)+((unit-100)*7)
else:
    bill = (100*5)+(100*7)+((unit-200)*10)
print("your bill :",bill)
    
    