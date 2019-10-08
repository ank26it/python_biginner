student = {'name': 'John', 'age': 23, 'courses':['Math', 'CompSci']}
print(student['courses'])
print(student['name'])
print(student['age'])

# print(student['phone']) #Error not insode student
print(student.get('phone'))
print(student.get('phone', 'Not Found'))


# Update value:
student2 = {'name': 'John', 'age': 23, 'courses':['Math', 'CompSci']}
#Student2['phone'] = '012-3456789' #Error not found
student2['name'] = 'Jane'
student2.update({'name': 'John', 'age': 26, 'phone': '012-3456789'})
print(student2)

# Remove Key:
del student2['phone']
print(student2)

# pop Key:
age = student2.pop('age')
print(student2)
print(age)

# see dictionary:
print(len(student2))
print(student2.keys())
print(student2.values())
print(student2.items())

for key in student2:
    print(key)

for key, value in student2.items():
    print(key, value)