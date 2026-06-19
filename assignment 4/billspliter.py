tba= float(input("enter a bill amount= "))
gst= int(input("enter gst= "))
sr= int(input("enter service charge= "))
fri= int(input("enter number of friends= "))
fgst=(tba/100)*gst
fsr=(tba/100)*sr
tba=tba+fsr+fgst
print("final bill= ",tba,"\neach person pays= ",tba/fri)