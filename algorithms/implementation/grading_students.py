"""
https://www.hackerrank.com/challenges/grading/problem
"""

import math


def is_grade_enough(grade):
    if rounded(grade) < 40:
        return(False)
    return(True)


def rounded(grade):
    if next_multiple_of_five(grade) - grade < 3:
        return(next_multiple_of_five(grade))
    return(grade)


def next_multiple_of_five(grade):
    if grade % 5 == 0:
        return(grade)
    next_multiple = math.ceil(grade/5)*5
    return(next_multiple)


students_number = int(input().strip())

for i in range(students_number):
    grade = int(input().strip())
    if is_grade_enough(grade):
        grade = rounded(grade)
    print(grade)
