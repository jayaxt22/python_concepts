n=int(input("enter no. of rows: "))
i=1
while i<=n:
    print()
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=i:
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j+=1
'''
      0
     01
    010
   1010
  01010
'''