'''
Docstring for Assignment21 - Strings IV.a07
Remove Duplicate Words from a String
Scenario

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

Write a Python program that removes duplicate words while maintaining the original order.

Input
hello hello how are are you
Output
hello how are you
'''

n=input("Enter The : ")

new=""

for w in n.split():
    if w not in new:
        new+=w+" "

print(new)