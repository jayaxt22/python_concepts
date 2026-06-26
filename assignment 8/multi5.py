a,b= map(int,input("enter a number= ").split(","))
count=0
for i in range(a,b+1):
    if i%5==0:
        count+=1
print("number of multiples:",count)   