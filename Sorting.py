li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li)
sr_li = sorted(li, reverse=True)
print('Sorted Variable:\t', s_li)
print('Sorted Variable2:\t', sr_li)
# li.sort()
# li.sort(reverse=True)
print('Original Variable:\t', li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t', s_tup)

di = {'name': 'wq', 'job': 'programming', 'age':None, 'os':'window'}
s_di = sorted(di)
print('Dict\t', s_di)

li2 = [-6,-5,-4,1,2,3]
s_li2 = sorted(li2)
s_li2abs = sorted(li2, key=abs)
print(s_li2) # if ignore neg then not work
print(s_li2abs)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Aris', 18, 70000)
e2 = Employee('Sira', 19, 60000)
e3 = Employee('Risa', 20, 50000)

employees = [e1,e2,e3]
# # 1:
# s_employees = sorted(employees) # error not work
# print(s_employees)

# # 2:
# def e_sort(emp):
#     return emp.name
# s_employees = sorted(employees, key=e_sort)
# print(s_employees)

# # 3:
# def e_sort(emp):
#     return emp.name
# s_employees = sorted(employees, key=e_sort, reverse = True)
# print(s_employees)

# # 4:
# s_employees = sorted(employees, key= lambda e: e.name)
# print(s_employees)

# 5:
from operator import attrgetter
s_employees = sorted(employees, key= attrgetter('age'))
print(s_employees)