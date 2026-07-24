'''
Docstring for a05
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
'''

website = input("Enter Website: ")
website = website.lower()

count = 0
length = len(website)

# Check www
if website[0] == "w" and website[1] == "w" and website[2] == "w":
    count += 3

# Check dots
if website[3] == "." and website[length - 4] == ".":
    count += 1

# Check com
if website[length - 3] == "c" and website[length - 2] == "o" and website[length - 1] == "m":
    count += 1

if count == 5:
    print("Valid Website")
else:
    print("Invalid Website")
        


        
