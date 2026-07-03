a=int(input("Enter Number Of Classes : "))
b=int(input("Enter Students Per Class : "))
c=int(input("Enter Subjects Per Student : "))
total=0

i=1
while i<=a:
    print(f"Class: {i}") 
    j=1
    while j<=b:
        print(f"  Student: {j}")
        k=0
        while k<c:
            m=int(input(f"\tEnter The Mark {k+1}: "))
            total+=m
            k+=1
        print(f"\tStudent: {j} ==> Total: {total}")
        total=0
        j+=1
    i+=1