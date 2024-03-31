n = "abcdefghijklmnopqrstuvwxyz"
m = input("Write your name:").lower()
o = input("Write your friend's name:").lower()

marks_1 = 0
for i in m:
    m = ord(i)-96
    marks_1 = marks_1+m
print("Here is your marks", marks_1)

marks_2 = 0
for j in o:
    o = ord(j)-96
    marks_2 = marks_2 + o
print("Here is friend's marks", marks_2)

