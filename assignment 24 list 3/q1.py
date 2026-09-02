for i in range(n):
    value=int(input("enter number:"))
    arr.append(value)
print(arr)


for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    
    if count==1:
        print(i)
else:    
    print("all number are repeating")    