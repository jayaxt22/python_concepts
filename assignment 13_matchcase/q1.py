while True:
    print("\n===== MENU =====")
    print("1. check prime number")
    print("2. check palindrome number")
    print("3. reverse number")
    print("4. count digits in number")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print("Checking prime number")
            num = int(input("Enter a number: "))
            if num > 1:                             
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        print(num, "is not a prime number")
                        break
                else:
                    print(num, "is a prime number")
        
         

        case "2":
            print("Checking palindrome number")
            num =int(input("number:"))
            tem=num
            reverse=0
            while num>0:
               rev=num%10
               reverse=reverse*10+rev
               num//=10
               
            if reverse==tem:
               print("palindrome")
            else:
             print("not a palindrome")

        case "3":
            a1 = int(input("Enter a number: "))
            rev=0
            while a1>0:
                rev = rev*10 + a1%10
                a1//=10
            print("Reversed number:", rev)

        case "4":
            count=0
            num = int(input("Enter a number: "))
            while num > 0:
                count += 1
                num //= 10
            print("Number of digits:", count)

        case "5":
            print("Exiting Program...")
            break

        case _:
            print("Invalid Choice")