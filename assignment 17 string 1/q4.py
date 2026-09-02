n=input("Enter Student Name : ").lower()

count=0

i=0
while i<len(n):
    if n[i] in "aeiou":
        pass
    else:
        count+=1
    i+=1

print(f"Total Consonants : {count}")