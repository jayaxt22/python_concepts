sub=input("enter subscription type (premium/basic: ")
pro=int(input("enter progress percent: "))
score=int(input("enter score:"))
if sub.lower()=="premium":
    if pro>=80:
        if score>=70:
           print("access status: grant certificate")
        else:
            print("acces status: retry test")
    else:
        print("access status :complete course first")
elif sub.lower()=="basic" :
     if pro>=50:
           print("access status: limited access")
     else:
           print("acces status: content locked")
else:
    print("access denied")