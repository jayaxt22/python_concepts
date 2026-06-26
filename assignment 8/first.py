n= int(input("enter number= "))
while n>=10:
    n//=10
print("first digit:",n)

'''
l=len(str(n))
# a=n//10**(l-1)
# print(a)

for i in range(l):
    if len(str(n))==1:
        print(n)
    n//=10
'''