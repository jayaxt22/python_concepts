'''
Docstring for a04
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5

'''
n=input("Enter The Complaint : ")
count=0

for word in n.split():
    # print(word)
    count+=1

print(count)