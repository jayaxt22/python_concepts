amt= int(input("enter amount you want to change= "))
hn = amt//100
fifty= (amt%100)//50
ten= (amt%50)//10
print("100 x ",hn,"\n50 x ",fifty,"\n10 x ",ten)