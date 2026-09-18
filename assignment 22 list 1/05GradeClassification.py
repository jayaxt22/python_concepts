"""
5. Student Grade Classification System (Python List Assignment)

Scenario

A school stores student marks in a list. The system must analyze
the marks and generate a clear performance report by grouping
students into grade categories.

Requirements

1. Iterate through the list of marks.
2. Assign grades based on marks:
- Marks >= 90       → A Grade
- Marks >= 75 < 90  → B Grade
- Marks >= 50 < 75  → C Grade
- Marks < 50        → Fail
3. Store each category in separate lists.
4. Count students in each category.
5. Display the final structured report.

Output Format (Mandatory)

===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X

Test Case

Input:
[95, 82, 67, 45, 30]

Expected Output:

===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5
"""
a_grade=[]
b_grade=[]
c_grade=[]
f_grade=[]
a_count=0
b_count=0
c_count=0
f_count=0

marks=[]
entry=input("enter the marks with space between them:").split()
marks.extend(map(int,entry))

for mark in marks:
    if mark >=90:
        a_count+=1
        a_grade.append(mark)
    elif mark<90 and mark >=75:
        b_count+=1
        b_grade.append(mark)
    elif mark<75 and mark >=50: 
        c_count+=1
        c_grade.append(mark)
    else:
        f_count+=1
        f_grade.append(mark)

print("===== STUDENT GRADE REPORT =====")
print()
print("A Grade Students   :",a_grade)
print("B Grade Students   :",b_grade)
print("C Grade Students   :",c_grade)
print("Fail Students      :",f_grade)
print()
print("--------------------------------")
print("A Count   :",a_count)
print("B Count   :",b_count)
print("C Count   :",c_count)
print("Fail Count:",f_count)
print("--------------------------------")
print()
print("Total Students:",len(marks))
