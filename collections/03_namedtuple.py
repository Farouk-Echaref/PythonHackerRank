#!/usr/bin/python3

# from collections import namedtuple


# Student = namedtuple('Student', ['name', 'age', 'ID'])

# ss = Student(name='fechcha', age='24', ID='69')

# print(ss)
# print(ss[0], ss[1], ss[2])
# print(ss.name, ss.age, ss.ID)

# Point = namedtuple('Point', 'x, y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)

# dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
# print (dot_product)

# print(pt1)
# print(pt2)
from collections import namedtuple

if __name__ == "__main__":
    N = int(input())
    total_students = N
    Student = namedtuple('Student', input().split())
    marks_sum = 0
    while N:
        data = input().split()
        si = Student(data[0], data[1], data[2], data[3])
        marks_sum += int(si.MARKS)
        N -= 1
    average = marks_sum / total_students
    print(round(average,2))