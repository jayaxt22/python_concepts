s= input("enter the string")
word= input("enter the word")
countu=0
i=0
while i<len(s):
    j=0
    while j<len(word):
        if s[i]==word[j]:
            j+=1
    if count==1:
        print(s[i])
        countu+=1
    i+=1
print("total unique",countu)