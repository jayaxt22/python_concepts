"""
6. Frequency Count of Elements (Advanced Scenario-Based Problem)

Scenario

A government survey department collects responses from different
regions. Each response is stored as an integer in a list
(representing selected option IDs).

The department wants to analyze:
1. How many times each option was selected.
2. Most popular option.
3. Least popular option.
4. Detect invalid entries (negative numbers or zeros).

Requirements

1. Store survey responses in a list.
2. Ignore invalid entries (<= 0).
3. Count frequency of each valid number.
4. Display frequency in sorted order.
5. Find the most frequently selected option.
6. Find the least frequently selected option.
7. Store frequency in a dictionary.

Note:
- Do NOT use the built-in Counter class.

Test Case 1

Input:
[1, 2, 2, 3, 3, 3, 4, 1, 2]

Expected Output:

Frequency Count:
1 -> 2
2 -> 3
3 -> 3
4 -> 1

Most Frequent: 2 or 3 (Tie)
Least Frequent: 4

--------------------------------------------------

Test Case 2

Input:
[1, 2, -1, 3, 0, 2, 4, -5, 3, 3]

Expected Output:

Invalid Entries Ignored: [-1, 0, -5]

Frequency Count:
1 -> 1
2 -> 2
3 -> 3
4 -> 1

Most Frequent: 3
Least Frequent: 1 or 4

--------------------------------------------------

Test Case 3

Input:
[5, 5, 5, 5, 2, 2, 1]

Expected Output:

Frequency Count:
1 -> 1
2 -> 2
5 -> 4

Most Frequent: 5
Least Frequent: 1

--------------------------------------------------

Test Case 4

Input:
[7, 7, 7, 7, 7]

Expected Output:

Frequency Count:
7 -> 5

Most Frequent: 7
Least Frequent: 7

--------------------------------------------------

Test Case 5

Input:
[-1, 0, -3]

Expected Output:

No valid data found
"""
numbers=[]
number=input("enter number with space between them:").split()
numbers.extend(map(int,number))

invalid=[]
frequency={}

for numb in numbers:
    if numb <=0:
        invalid.append(numb)
    else:
        if numb in frequency:
            frequency[numb] += 1
        else:
            frequency[numb] = 1

if invalid:
    print("Invalid Entries Ignored:",invalid)

if not frequency:
    print("no valid data found")
else:
    print("frequancy count:")
    for values in sorted(frequency):
        print(values,"-->",frequency[values])

max_frequancy=max(frequency.values())        
min_frequancy=min(frequency.values())  

most_frequent = []

for option in frequency:
    if frequency[option] == max_frequancy:
        most_frequent.append(option)

# Find all options with minimum frequency
least_frequent = []

for option in frequency:
    if frequency[option] == min_frequancy:
        least_frequent.append(option)

print("Most Frequent:", most_frequent)
print("Least Frequent:", least_frequent)