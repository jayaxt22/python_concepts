n=5

for i in range(n,0,-1):
    x=65
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x+=1
    print()
'''
A B C D E 
A B C D 
A B C 
A B 
A  
'''