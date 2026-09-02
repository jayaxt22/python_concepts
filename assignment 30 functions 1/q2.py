def factorial(number):
    p=1
    for i in range(1,number+1):
        p*=i
	
    return p

def primes(number):

    prime=False
    if number<1:
        prime= False
    else:
        for i in range(2,number):
            if number%i==0:
                prime=False
                break
            else:
                prime=True
    return prime

def perfects(number):
    temp=number
    fact=0
    if number<1:
        perfect=False
    else:
        for i in range(1,number):
            if number%i==0:
               fact+=i

    if temp==fact:
        perfect=True
    else:
        perfect=False  
    return perfect    

def factors(numbers):

    fact=''
    if number<1:
        print("number is negative ")

    else:
        for i in range(1,number):
            if number%i==0:
                fact+=str(i)+" ,"
    return fact 

def reverse(number):

    sum=0
    while number>0:

        
        rev=number%10
        sum=sum*10+rev
        number//=10
    return sum
   

while True:
    
    print("============================================")
    print("1. check Perfect Number")
    print("2. check Prime Number")
    print("3. Find Reverse of a number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. EXIT")
    print("=============================================")
    choice=int(input("enter choice:"))

    match choice:

        case 1 :
                print("==========check perfect number==========")
                number=int(input("enter the number"))
                print("========================================")
                print(perfects(number))
                print("========================================")

        case 2 :
                print("=========Check Prime Numner===========")
                number=int(input("enter the number:"))
                if primes(number)==True:
                    print("Prime Number")
                else:
                    print("Not a Prime Number")
                print("==========================================")    
        case 3 :
                print("=========Reverse a Number==========")
                number = int(input("enter the number:"))
                print("Reverse Of Number:",reverse(number))
        case 4 :
                print("==========calculate Factorial==========")
                number = int(input("enter the number:"))
                print(f"facotrial of {number} : {factorial(number)}")
                print("=======================================")
        case 5 :
                print("===========Factorial Of Number===========")
                print()
                number=int(input("enter the number:"))
                print("factor of the number: ",factors(number))
                print()
                print("=======================================")
        case 6 :
            print("======program is terminated======")
            break
        case _ :
            print("invalid choice!\ntry again")