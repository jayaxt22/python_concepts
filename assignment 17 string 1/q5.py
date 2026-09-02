n=input("Enter The Password : ")
upper=0
digit=0
count=0
special=0
space=0
i=0
while i<len(n):
    if n[0]>="A" and n[0]<="Z":
        upper=1
    elif n[len(n)-1]>="0" :
        digit=1
    elif n[i]>="0" and n[i]<="9":
        count+=1
    elif n[i] in "@#$%&*":
        special=1
    elif n[i]==" ":
        space=1
    else:
        pass
    i+=1

if upper==1 and digit==1 and count>=2 and special==1 and space==0 and(len(n)>=8 and len(n)<=15) :
    print("valid")

else:
    print("invalid")