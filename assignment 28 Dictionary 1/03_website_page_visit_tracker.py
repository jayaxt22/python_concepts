# Q3. WEBSITE PAGE VISIT TRACKER
# Count visits of each page using a dictionary and display
# the page name with its visit count.
# pages = ["Home","About","Home","Contact","Home","About"]

# pages = ["Home", "About", "Home", "Contact", "Home", "About"]

# Write your solution below
pages = eval(input("Enter list : "))
data = {}

for i in pages:
    if i in data:
        # Get Func Jaruri nhi hai hmesha 
        data[i]+=1
    else:
        data[i]=1

for key , value in data.items():
    print(f"{key} visited {value} times")