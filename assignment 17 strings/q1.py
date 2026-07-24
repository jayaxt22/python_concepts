s= input("enter a string:")
count=0
for i in range(len(s)):
    if s[i] in 'aeiou' or s[i] in 'AEIOU':
        count+=1
print("count of vowels",count) 