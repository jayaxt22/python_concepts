patient={}
while True:
    print("1. Add New Patient")
    print("2. Search Patient")  
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")

    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            print("Add New Patient")
            id = int(input("enter new patient id: "))
            if id in patient:
                print("patient id already exist:")
            else:
                name=input("enter the name of patient:")
                age=int(input("enter the age:"))
                gender=input("enter the gender:")
                disease=input("enter the disease of the patient:")
                docter=input("enter the docter's name:")

                patient[id]={
                    "name": name,
                    "age": age,
                    "gender":gender,
                    "disease":disease,
                    "docter":docter
                } 
                print("Patient Added successfully!")   
        case 2:
            print("===========SEARCH PATIENT===========")
            ID = int(input("enter patient id:"))
            if ID in patient:
                    print("=====================================")               
                    print("\nID:", ID)
                    print("Name:", patient[ID]["name"])
                    print("Age:", patient[ID]["age"])
                    print("Gender:",patient[ID]["gender"])
                    print("Disease:", patient[ID]["disease"])
                    print("Docter:", patient[ID]["docter"])
                    print("=====================================")
            else:
                print("patient doesnot exist!")        
        case 3:
            print("============UPDATE PATIENT DISEASE=============")
            ID=int(input("enter patient id:"))
            if ID in patient:
                    print("=====================================")               
                    print("\nID:", ID)
                    print("Name:", patient[ID]["name"])
                    print("Age:", patient[ID]["age"])
                    print("Gender:",patient[ID]["gender"])
                    print("Disease:", patient[ID]["disease"])
                    print("Docter:", patient[ID]["docter"])
                    print("=====================================")
                    des=input(f"enter new  disease for the patient {patient[ID]["name"]}:")
                    patient[ID]["disease"]=des


        case 4:
            print("========DELETE PATIENT RECORD===========")
            ID=int(input("enter patient id to delete:"))
            if ID in patient:
                del patient[ID]
                print("successfully deleted patient record!")
                for pid,details in patient.items():
                   print("===============================")
                   print("Id:",pid)
                   print("Name:",details["name"])
                   print("Age:",details["age"])
                   print("Gender:",details["gender"])
                   print("Disease:",details["disease"])
                   print("Docter:",details["docter"])
                   print("================================")
            else:
                print("patient doesnot exist!")    
        case 5:
            print("===========All Patients============")
            for pid,details in patient.items():
                print("===============================")
                print("Id:",pid)
                print("Name:",details["name"])
                print("Age:",details["age"])
                print("Gender:",details["gender"])
                print("Disease:",details["disease"])
                print("Docter:",details["docter"])
                print("================================")
            print("====================================")    
        case 6:
            print("====================================")
            print("Total Patients:",len(patient))
            print("====================================")
        case 7:
            print("=====LIST OF PATIENT BY DISEASE=====")
            disease=input("enter the disease:")
            for pid,details in patient.items():
                if disease in patient[pid]["disease"]:
                    print("=====================================")               
                    print("\nID:", pid)
                    print("Name:", patient[pid]["name"])
                    print("Age:", patient[pid]["age"])
                    print("Gender:",patient[pid]["gender"])
                    print("Disease:", patient[pid]["disease"])
                    print("Docter:", patient[pid]["docter"])
                    print("=====================================")
                    

        case 8:
            print("===========oldest patient==============")
            
            oldest=None
            for pid,details in patient.items():
                if oldest is None or details["age"]<patient[oldest]["age"] :
                    oldest=pid


            print("=====================================")
            print("Name:", patient[oldest]["name"])
            print("=====================================")

        case 9:
            print("===============youngest patient===============")
            youngest=None
            for pid,details in patient.items():
                if youngest is None or details["age"]<patient[youngest]["age"] :
                    youngest=pid


            print("=====================================")
            print("Name:", patient[youngest]["name"])
            print("=====================================")

        case 10:
            print("thank you for using hospital patient record management system.\nexiting program!!")
            break
        case _:
            print("invalid choice\n exiting program!!")