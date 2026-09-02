
r1,c1=map(int,input("Enter The Row 1 And Column 1 : ").split(" "))
r2,c2=map(int,input("Enter The Row 1 And Column 1: ").split(" "))

print("Fill The 1st Matrix")
arr1=[]
for i in range(r1):
    row=list(map(int,input(f"Enter The Element in {i+1}th Row : ").split(" ")))
    arr1.append(row)

print("Fill The 2st Matrix")
arr2=[]
for i in range(r2):
    row=list(map(int,input(f"Enter The Element in {i+1}th Row : ").split(" ")))
    arr2.append(row)

print("First Matrix",arr1)  
print("Second Matrix",arr2) 
while True:
    print("\n1. Add Two Matrices")
    print("2. Subtract Two Matrices")
    print("3. Compare Two Matrices")
    print("4. Exit")

    choice = input("Enter your choice: ")



    match choice:

        case "1":

            if r1 != r2 or c1 != c2:
                print("Matrices cannot be added.")
                continue
            c=[]

            for i in range(len(arr1)):
                row=[]
                sum=0
                for j in range(len(arr1[i])):
                    sum=arr1[i][j]+arr2[i][j]
                    row.append(sum)
                c.append(row)
            
            print("Result Matrix:")
            for row in c:
                print(*row)

                
                    


        case "2":


            if r1 != r2 or c1 != c2:
                print("Matrices cannot be subtracted.")
                continue
            c=[]

            for i in range(len(arr1)):
                row=[]
                sum=0
                for j in range(len(arr1[i])):
                    sum=arr1[i][j]-arr2[i][j]
                    row.append(sum)
                c.append(row)
            
            print("Result Matrix:")
            for row in c:
                print(*row)

        case "3":
            
            if r1 != r2 or c1 != c2:
                print("Matrices are Not Equal")
                continue
            equal=True
            for i in range(len(arr1)):
                for j in range(len(arr1[i])):
                    if arr1[i][j]!=arr2[i][j]:
                        equal=False
                        break
                
            if equal:
                print("Matrices Are Equal")
            else:
                print("Matrices Are Not Equal")    


        case "4":
            print("Thank You for Using Matrix Operations Management System")
            break

        case _:
            print("Invalid Choice")