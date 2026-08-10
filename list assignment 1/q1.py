n= int(input("enter length of list: "))
rec=[]
for i in range(n):
    num= int(input("enter marks: "))
    rec.append(num)
print(rec)    
large=0
small=0
count=0
for i in rec:
    if i>large:
        large=i
    if i<small:
        small=i
for i in rec:
    if i>=75:
       count+=1
print("above 75 marks students=",count)       
print("largest= ",large)
print("smallest = ", small)