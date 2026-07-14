
n=5
for i in range(1,n+1):
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print()    
'''
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
'''