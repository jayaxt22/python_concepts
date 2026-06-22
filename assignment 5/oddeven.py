num = int(input("enter number: "))
if num%2 == 0:
     print("even number")
     if num%5 ==0:
        print("divisible by 5")
     else:
        print("not  divisible by 5")
else:
    print("odd number")
    if num%5 ==0:
        print("divsible by 5")
    else:
        print("not divisible by 5")