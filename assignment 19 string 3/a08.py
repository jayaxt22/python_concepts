'''
Docstring for a08
SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================

Program Closed Successfully
'''

while True:
    print("1. Reverse Complete String")
    print("2. Reverse Every Word")
    print("3. Reverse Word Order")
    print("4. Exit")

    ch = int(input("Enter Choice : "))

    match ch:

        case 1:
            print("Choice 1")
            s=input("Enter String : ")         

           
            chars = ""
            for ch in s:
                if ch.isalnum():
                    chars += ch

            print(chars)

           
            rev = ""
            i = len(chars) - 1
            while i >= 0:
                rev += chars[i]
                i -= 1
            
            print(rev)

            
            ans = ""
            j = 0

            for ch in s:
                if ch.isalnum():
                    ans += rev[j]
                    j += 1
                else:
                    ans += ch

            print(ans)

            

        case 2:
            print("Choice 2")
            n=input("Enter : ")
            result=""
            for i in n.split():
                digit = False

                for ch in i:
                    if '0' <= ch <= '9':
                        digit = True
                        break
                
                if digit:
                    result+=i+" "
                else:
                    rev=""
                    for j in range(len(i)-1,-1,-1):
                        
                        rev+=i[j]
                    if 'a'<=rev[0]<='z':
                         rev = chr(ord(rev[0]) - 32) + rev[1:]
                    
                    result+=rev+" "
            print(result)
                
                


            

        case 3:
            print("Choice 3")

            n = input("Enter : ")

            result = ""
            seen = ""

            for word in n.split():

                found = False

            
                for w in seen.split():
                    if word.lower() == w.lower():
                        found = True
                        break

                if not found:
                    seen += word + " "

        
            words = seen.split()

            for i in range(len(words) - 1, -1, -1):
                print(words[i], end=" ")
            print()


            

        case 4:
            print("Program Closed Successfully")
            break

        case _:
            print("Invalid Choice")