marks= int(input("enter marks:"))
att = int(input("enter attendence: "))
if marks >= 40:
    if att >= 75:
        print("eligible for certificate")
    else:
        print("not eligible")
   print("pass")        
else:
    print("fail")