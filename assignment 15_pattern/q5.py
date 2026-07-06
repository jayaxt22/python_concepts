n=int(input("enter no. of rows: "))
i=1
while i<=n:
    
    j=1
    while j<i:
        print(" ",end="")
        j+=1 
    k=n
    while k>=i:
        print(k,end="")
        k-=1
    print()  
    i+=1