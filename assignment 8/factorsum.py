n= int(input("enter a number:"))
count=0
'''
for i in range(1,n+1):
    if n%i==0:
        count+=1
print("factor count=",count)  
'''
i=1
while n>=i:
       if n%i==0:
        count+=i
       i+=1    
print("sum=",count)

  
   