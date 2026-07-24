# Reverse Sentence + Reverse Each Word
# Scenario

# Secret Military Communication Decoder

# A defense organization stores highly confidential messages in encrypted form.

# To decode the message:

# Reverse the entire sentence.
# Reverse every individual word.
# Store the final result back into the original string variable.

# Condition

# You must use the split() method.
# Input
# Python is powerful
# Output
# lufrewop si nohtyP

n=input("Enter The :")
sent=""
for word in n.split():

    rev=""
    for i in range(len(word)-1,-1,-1):
        rev+=word[i]
    if sent == "":
        sent = rev
    else:
        sent = rev + " " + sent

    
print(sent, end=" ")

