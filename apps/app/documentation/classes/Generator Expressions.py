# https://docs.python.org/3/tutorial/classes.html
# sum of squares
sos = sum(i * i for i in range(10))
print(sos)
print("==========================")
xvec = [10, 20, 30]
yvec = [7, 5, 3]
# dot product
dp = sum(x * y for x, y in zip(xvec, yvec))
print(dp)
print("==========================")
from math import pi, sin

sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}
print(sine_table)
print("==========================")
page = open("Lorem Ipsum.txt", 'r')
unique_words = set(word for line in page for word in line.split())
print(unique_words)
print("==========================")


class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


graduates = []
for index in range(100):
    student = Student("Student" + " " + str(index), index)
    graduates.append(student)
valedictorian = max((student.gpa, student.name) for student in graduates)
print(valedictorian)
print("==========================")
data = 'golf'
lst = list(data[i] for i in range(len(data) - 1, -1, -1))
print(lst)
print("==========================")
