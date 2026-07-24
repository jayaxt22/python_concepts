'''
Docstring for a07
Advanced Smart Chat Compression Expansion System

A messaging application stores repeated characters in compressed form to
reduce storage space. Before displaying messages to users, the system
should reconstruct the original message.

The application team has introduced additional rules.

Conditions: - Alphabet followed by number - Repeat character according
to the number - If alphabet is uppercase convert expanded characters
into lowercase - Ignore special symbols - Display expanded string -
Display total character count

Test Case 1 Input: Enter compressed message: a3

Output: Expanded Message: aaa

Total Characters: 3

Test Case 2 Input: Enter compressed message: A4b5

Output: Expanded Message: aaaabbbbb

Total Characters: 9

Test Case 3 Input: Enter compressed message: x2Y3

Output: Expanded Message: xxyyy

Total Characters: 5

Test Case 4 Input: Enter compressed message: m5@n2P4

Output: Expanded Message: mmmmmnnpppp

Total Characters: 11

Test Case 5 Input: Enter compressed message: R3S2t5

Output: Expanded Message: rrrssttttt

Total Characters: 10
'''


n = input("Enter  Code : ")

s = ""
b=""
m = ""


for i in range(len(n)):
    if n[i] not in "!@#$%^&*-_ ":
        if 'A' <= n[i] <= 'Z':
            s +=  chr(ord(n[i]) + 32)
        else:
            s += n[i]

print(s)

for i in range(len(s)):

    if 'a'<=s[i]<='z' and s[i+1] in "0123456789":
        num=int(s[i+1])
        a=s[i]
        for j in range(num):
            b+=a
        

print(f"Expanded : {b}")
print(f"Total Count : {len(b)}")


