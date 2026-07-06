n=int(input("enter no. of rows: "))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("0",end="")
        else:
            print("1",end="")
        
        j+=1
    i+=1 