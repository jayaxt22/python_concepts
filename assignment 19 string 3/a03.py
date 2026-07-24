'''
Docstring for a03
 Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
'''

n=input("Enter The Name : ")
s=""

for i in range (len(n)):
   
   if n[i]==" ":
      print(i)
      r=""
               
      count=0

      for j in range (i-1,-1,-1):

        if n[j]==" ":
            count+=1
        else:
           break
      print(count)
    
      if count==0 and i!=0:
         s+=n[i]
      
   else:
      s+=n[i]

print(s)
print(n)