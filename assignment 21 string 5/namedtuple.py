from collections import namedtuple
Acount=namedtuple("acount", ["accno","holdername","balance"])
accounts=[]

no=int(input("enter number:"))
for i in range(no):

    print("enter details: below")
    name=input("enter name:") 
    balance=int(input("enter balance:"))
    accnum=int(input("enter account no:"))
    acc=Acount(accnum,name,balance)
    accounts.append(acc)
print(accounts)
for x in  accounts:
    print(x)