s= input("enter a string:")
ch =input("enter character: ")
count=0
for i in range(len(s)):
    if s[i] == ch :
        count+=1 
print(f"character {ch } occurs {count } times")        
        