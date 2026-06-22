num = input("membership active (yes/no): ")
books = int(input("book issued : "))
num= num.lower()
if num == "yes":
   print("entry allowed")
   if books >= 3:
       print("can't issue books limit reached")
   else:
       print("can issue more books")
else:
    print("entry not allowed")

