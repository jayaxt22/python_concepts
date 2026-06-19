pprice= float(input("enter a product price= "))
dop= int(input("enter downpayment paid= "))
interest= int(input("enter interest rate= "))
month= int(input("enter months= "))
rp= pprice-dop
fa= rp+(rp/100)*interest
emi=fa/month
print("remaining amount= ",rp,"\ntotal with interest= ",fa,"\nmonthly EMI =",emi)