
n=5
for i in range(1,n+1):
    space=5
    for s in range(5,space-i,-1):
       print("",end="")
       for j in range(n,n-i,-1):
           print("*",end="")
    print()    
'''
*
****
*********
****************
************************* 
'''