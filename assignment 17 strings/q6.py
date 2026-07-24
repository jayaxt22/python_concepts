n=input("enter the PNR : ")
c=0
if len(n)==12:
    if n.startswith("PNR"):
        i=3
        while i<len(n):
            if not (n[i]>='0' and n[i]<='9'):
                c=1
                break
            
            i+=1
    if c==1:
        print("invalid")
    else:
        print("valid")
else:
    print("Invalid length")