# # 1:
# import my_module

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = my_module.find_index(courses, "Math")
# print(index)

# # 2:
# import my_module as mm

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, "Math")
# print(index)

# # 3:
# from my_module import find_index

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, "Math")
# print(index)

# # 4:
# from my_module import find_index, test

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, "Math")
# print(index)
# print(test)

# # 5:
# from my_module import find_index as fi, test

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = fi(courses, "Math")
# print(index)
# print(test)

# # 6 import everything:
# from my_module import *

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = fi(courses, "Math")
# print(index)
# print(test)

# 7:
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

print(random_course)

# 8:
import math

rads = math.radians(90)
print(math.sin(rads))

# 9:
import datetime
import calendar

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# 10:
import os

print(os.getcwd())
print(os.__file__)

