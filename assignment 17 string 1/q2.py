
s= input("enter a string:")
count=0
for i in range(len(s)):
    if s[i] in ' ':
        count+=1 
print("count of space",count)        
        