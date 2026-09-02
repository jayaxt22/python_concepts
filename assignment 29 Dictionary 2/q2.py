students={}
while True:
    print("=================================")
    print("STUDENT MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Add New Student")
    print("2. Search Student")  
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Student")
    print("6. Count Total Students")
    print("7. Display Students By course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10.Find Student Paying Lowest Fees")
    print("11. Exit")

    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            print("Add New Student")
            id = int(input("enter new Student id: "))
            if id in students:
                print("Student id already exist:")
            else:
                name=input("enter the name of student:")
                cname=input("enter the course:")
                mob=int(input("enter the mobile number:"))
                fees=int(input("enter the fees of the student:"))
                city=input("enter the city:")

                students[id]={
                    "name": name,
                    "cname": cname,
                    "mob":mob,
                    "fees":fees,
                    "city":city
                } 
                print("Student Added successfully!")   
        case 2:
            print("===========SEARCH STUDENT===========")
            ID = int(input("enter Student id:"))
            if ID in students:
                    print("=====================================")               
                    print("\nID:", ID)
                    print("student Name:", students[ID]["name"])
                    print("course name:", students[ID]["cname"])
                    print("mobile number:",students[ID]["mob"])
                    print("fees:",students[ID]["fees"])
                    print("city:", students[ID]["city"])
                    print("=====================================")
            else:
                print("Student doesnot exist!")        
        case 3:
            print("============UPDATE STUDENT COURSE=============")
            ID=int(input("enter student id:"))
            if ID in students:
                    print("=====================================")               
                    print("\nID:", ID)
                    print("Name:", students[ID]["name"])
                    print("course:", students[ID]["cname"])
                    print("mobile number:",students[ID]["mob"])
                    print("fees:",students[ID]["fees"])
                    print("city:", students[ID]["city"])
                    print("=====================================")
                    new=input(f"enter new Course for {students[ID]["name"]}:")
                    students[ID]["cname"]=new


        case 4:
            print("========DELETE STUDENT RECORD===========")
            ID=int(input("enter student id to delete:"))
            if ID in students:
                del students[ID]
                print("successfully deleted student record!")
                for sid,details in students.items():
                   print("===============================")
                   print("Id:",sid)
                   print("Name:",details["name"])
                   print("Course:",details["cname"])
                   print("Mobile number:",details["mob"])
                   print("fees:",details["disease"])
                   print("city:",details["city"])
                   print("================================")
            else:
                print("Student doesnot exist!")    
        case 5:
            print("===========All Students============")
            for sid,details in students.items():
                print("===============================")
                print("Id:",sid)
                print("Name:",details["name"])
                print("Course:",details["cname"])
                print("Mobile Number:",details["mob"])
                print("Fees:",details["fees"])
                print("City:",details["city"])
                print("================================")
            print("====================================")    
        case 6:
            print("====================================")
            print("Total Students:",len(students))
            print("====================================")
        case 7:
            print("=====LIST OF STUDENT BY COURSE=====")
            course=input("enter the course:")
            for sid,details in students.items():
                if course in students[sid]["cname"]:
                    print("=====================================")               
                    print("\nID:", sid)
                    print("Name:", students[sid]["name"])
                    print("Course:", students[sid]["cname"])
                    print("mobile number:",students[sid]["mob"])
                    print("Fees:", students[sid]["fees"])
                    print("City:", students[sid]["city"])
                    print("=====================================")
                else:
                    print("No student in this course!")    
                    

        case 8:
            print("===========LIST OF STUDENT BY CITY==============")
            city=input("enter the city:")
            for sid,details in students.items():
                if city in students[sid]["city"]:
                    print("=====================================")               
                    print("\nID:", sid)
                    print("Name:", students[sid]["name"])
                    print("Course:", students[sid]["cname"])
                    print("mobile number:",students[sid]["mob"])
                    print("Fees:", students[sid]["fees"])
                    print("City:", students[sid]["city"])
                    print("=====================================")
                else:
                    print("No student from the city enterd!")
                
        case 9:
            print("===============Highest paying Student===============")
            highest=None
            for sid,details in students.items():
                if highest is None or details["fees"]>students[highest]["fees"] :
                    highest=sid


            print("=====================================")
            print("Name:", students[highest]["name"])
            print("=====================================")

        case 10:
            print("=======Lowest fees paying student======= ") 
            lowest=None
            for sid,details in students.items():
                if lowest is None or details["fees"]<students[lowest]["fees"] :
                    lowest=sid


            print("=====================================")
            print("Name:", students[lowest]["name"])
            print("=====================================")
        case 11:
            print("thank you for using student record management system.\nexiting program!!")
            break   
        case _:
            print("invalid choice\ntry again!!")