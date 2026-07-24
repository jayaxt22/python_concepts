n=5
i=1

for i in range(1,n+1):
    x=65
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print(chr(x),end=" ")
        x+=1
    print()    
'''
    A 
   A B C 
  A B C D E 
 A B C D E F G 
A B C D E F G H I 
'''