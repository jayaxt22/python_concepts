a=int(input("Enter Number a: "))
b=int(input("Enter number b: "))
while a<=b:
    n=a
    rev=0
    while n>0:
        digit=n%10
        rev= rev*10+digit
        n//=10
    if rev==a:
      print(rev)
    a+=1 