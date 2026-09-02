name=None
roll=None
mk1=0
mk2=0
mk3=0
mk4=0
mk5=0
totalmarks=0
highest=0
lowest=100
grades=''

def display():
    global name,roll,mk1,mk2,mk3,mk4,mk5

    print("----------- RESULT CARD -----------")
    print()
    print("Name        :", name)
    print("Roll Number :", roll)
    print()
    print("Marks")
    print("Subject 1 :", mk1)
    print("Subject 2 :", mk2)
    print("Subject 3 :", mk3)
    print("Subject 4 :", mk4)
    print("Subject 5 :", mk5)
    print()
    print("Total Marks :", totalmarks)
    print("Percentage  :", percentage(),"%")
    print("Grade       :", grade())
    print("Highest Mark:", high())
    print("Lowest Mark :", low())

    print("------------------------------------")
        
def detail():

       global name,roll,mk1,mk2,mk3,mk4,mk5

       name=input("enter the name:")
       roll=int(input("enter the roll number:"))
       mk1=int(input("enter marks 1:"))
       mk2=int(input("enter marks 2:"))
       mk3=int(input("enter marks 3:"))
       mk4=int(input("enter marks 4:"))
       mk5=int(input("enter marks 5:"))
       
       return print("\nstudent added succesfully!")

def total():
    global totalmarks
    totalmarks=mk1+mk2+mk3+mk4+mk5
    return print("Total Marks = ",totalmarks)

def percentage():
    calcpercent=lambda tm:(tm/500)*100
    percent=calcpercent(totalmarks)
    return percent

def high():
    global mk1,mk2,mk3,mk4,mk5,highest
    marks=[mk1,mk2,mk3,mk4,mk5]
    
    for num in marks:
        if num>highest:
            highest=num
    return highest   

def low():
    global mk1,mk2,mk3,mk4,mk5,lowest
    marks=[mk1,mk2,mk3,mk4,mk5]
    
    for num in marks:
        if num<lowest:
            lowest=num
    return lowest      

def grade():

    global grades
    if percentage() >=90:
        grades='A+'
    elif percentage() >= 80 and percentage() <=89:
        grades='A'
    elif percentage() >= 70 and percentage() <=79:
        grades='B'
    elif percentage() >= 60 and percentage() <=69:
        grades='C'
    elif percentage() >= 50 and percentage() <=59:
        grades='D'
    else:
        grades="fail"

    return grades





while True:
    
    print("============================================")
    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Find Grade")
    print("5. Display Complete Result")
    print("6. Find Highest Subject Mark")
    print("7. Find Lowest Subject Mark")
    print("8. Exit")
    print("=============================================")
    choice=int(input("enter choice:"))

    match choice:

        case 1 :
                print("==========ADD STUDENT REPORT==========")
                detail()
        case 2 :
                total()
        case 3 :
                print("percentage = ",percentage(),"%")
        case 4 :
                print("Grade :",grade())
        case 5 :
                display()
        case 6 :
                print("Highest Marks :",high())
        case 7 :
                print("Lowest Marks :",low())
        case 8 :
            print("======thank you for using student result portal======")
        case _ :
            print("invalid choice!\ntry again")