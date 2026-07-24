'''
Docstring for a04
Instant Messaging Word Encryption System

Input : java is powerful
Output: avaj si lufrewop
'''

n = input("Enter The Message : ")

s = ""
word = ""

for i in range(len(n)):

    if n[i] != " ":
        word += n[i]

    else:
        
        for j in range(len(word) - 1, -1, -1):
            s += word[j]

        s += " "
        word = ""


for j in range(len(word) - 1, -1, -1):
    s += word[j]

print("Encrypted Message :", s)