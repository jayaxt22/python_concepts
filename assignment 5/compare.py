#nested if else 
a = int(input("enter quantity of a: "))
b = int(input("enter quantity of b: "))
c = int(input("enter quantity of c: "))
d = int(input("enter quantity of d: "))
e = int(input("enter quantity of e: "))
f = int(input("enter quantity of f: "))
if a>b:
    if a>c:
         if a>d:
             if a>e:
                 if a>f:
                     print("highest stock= ",a)
                 else:
                     print("highest stock= ",f)
else:
    if b>c:
        if b>d:
            if b>e:
                if b>f:
                    print("highest stock= ",b)
                else:
                    print("highest stock= ",f)
    else:
        if c>d:
            if c>e:
                if c>f:
                    print("highest stock= ",c)
                else:
                    print("highest stock= ",f)
        else:
            if d>e:
                if d>f:
                    print("highest stock= ",d)
                else:
                    print("highest stock= ",f)
            else:
                if e>f:
                    print("highest stock= ",e)
                else:
                    print("highest stock= ",f)
    
        