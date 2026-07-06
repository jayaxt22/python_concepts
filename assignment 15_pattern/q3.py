n=int(input("enter no. of rows: "))
i=1
while i<=n:
    
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1 
    k=1
    while k<=i:
        print("*",end="")
        k+=1
    print()  
    i+=1 
 '''
      *
     **
    ***
   **** 
  *****
 ******
'''