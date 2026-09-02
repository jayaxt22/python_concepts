# Q9. INVENTORY MANAGEMENT SYSTEM
# Display products having stock less than 30.
# stock = {"Pen":50,"Pencil":100,"Eraser":25,"Marker":10}

# stock = {
#     "Pen": 50,
#     "Pencil": 100,
#     "Eraser": 25,
#     "Marker": 10
# }

# Write your solution below
stock = eval(input("Enter list : "))
ans = {}

for i,v in stock.items():
    if v<=30:
        ans[i]=v

for i in ans:
    print(i)