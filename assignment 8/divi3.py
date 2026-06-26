a,b= map(int,input("enter number= ").split(","))
for i in range(a,b):
    if i%3==0:
        print(i,end=(","))