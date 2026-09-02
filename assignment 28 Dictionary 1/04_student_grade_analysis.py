# Q4. STUDENT GRADE ANALYSIS
# Find the student with the highest marks and the student
# with the lowest marks.
# Output: Highest Marks : Ravi 92
#         Lowest Marks : Aman 65

# students = {
#     "Ajay": 78,
#     "Ravi": 92,
#     "Neha": 85,
#     "Aman": 65
# }

# Write your solution below

pages = eval(input("Enter list : "))

Highest=0
Highest_S=""
Lowest=list(pages.values())[0]
Lowest_S=""

for k,v in pages.items():
    if v > Highest:
        Highest=v
        Highest_S=k
    if v < Lowest:
        Lowest=v
        Lowest_S=k

print(" Highest Marks : ",Highest_S,Highest)
print(" Lowest Marks :",Lowest_S,Lowest)