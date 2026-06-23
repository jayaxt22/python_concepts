#nested if else 
salary = int(input("enter your salary: "))
cred = int(input("enter credit score: "))
num = int(input("enter no. of existing loans: "))
if salary >= 30000:
         if cred >= 750:
              print("loan status = loan approved")
         else:
             if num<2:
                 print("loan status = conditional approval")
             else:
                 print("loan status = rejected ")
else:
    print("loan status = rejected")
          