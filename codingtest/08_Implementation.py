from tkinter import X


S = sorted(input())
alphabet = ""
number = 0
for x in S:
    if x.isalpha():
        alphabet += x
for y in S:
    if y.isdecimal():
        number += int(y)
print(alphabet + str(number))