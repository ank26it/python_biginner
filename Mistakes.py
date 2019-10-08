
# # space + space + space + space vs Tab:
# # in VSCode not problem:
# nums= [11, 30, 44, 54]

# for num in nums:
#     square = num ** 2
#     print(square)

# # module name same with library name:
# # if your module name is math:
# # the compiler find your module 1st then library:
# # so that following code should get error:
# from math import radians, sin
# rads = radians(90)
# print(sin(rads))

# # method() name same with define variable name:
# from math import radians, sin
# radians = radians(90) # error here
# rad45 = radians(45)
# print(rad45)


# # why cant create new list:
# def add_employee(emp, emp_list=[]): # just run one time
#     emp_list.append(emp) # so its keep adding on a same list
#     print(emp_list)
# # emps = ['John', 'Jane']
# add_employee('wq')
# add_employee('et')
# add_employee('hola')
# # solution:
# def add_employee(emp, emp_list=None):
#     if  emp_list is None:
#         emp_list = []# so its run every loop
#     emp_list.append(emp) 
#     print(emp_list)
# emps = ['John', 'Jane']
# add_employee('wq',emps )
# add_employee('et')
# add_employee('hola')

# # other example for Time:
# import time
# from datetime import datetime

# def display_time(time=datetime.now()):
#     print(time.strftime('%B %d, %Y %H:%M:%S'))
# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)
# display_time() # same time even though being delay 
# # Solution:
# def display_time(time=None):
#     if time is None:
#         time = datetime.now()
#     print(time.strftime('%B %d, %Y %H:%M:%S'))
# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)
# display_time()

# # Iterator data destroy afther runing one time: python2 vs python3 
# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# identities = zip(names, heroes)
# print(identities) # python2 printed python3 not
# print(list(identities)) # print for python3

# '''after printed expect print again in for loop but not'''
# for identity in identities:
#     print('{} is actually {}'.format(identity[0], identity[1]))

# # Solution:
# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# identities = list(zip(names, heroes)) # store early in list:
# print(identities)

# '''after printed expect print again in for loop now work'''
# for identity in identities:
#     print('{} is actually {}'.format(identity[0], identity[1]))

# same method() name from both library:
# do not use from {lib} import *
# just import needed fountion from {lib} import {name}
# from html import *
# from glob import *
# '''confuse people reading ur code hard to find which function'''
# print(help(escape))
# use this way:
from html import escape as h_escape
from glob import escape as g_escape
print(help(g_escape))
# or
import html
import glob
print(html.escape)
print(glob.escape)

