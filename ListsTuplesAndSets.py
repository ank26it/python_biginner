# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses2 = ['History2', 'Math2']
# nums = [1, 5, 2, 4, 3]

# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[3])
# print(courses[-1])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])

# # add item into a list:
# courses.append('Art')
# print(courses)
# courses.insert(0, 'Electronic')
# print(courses)

# # insert list into a list:
# # courses.insert(0,courses2)
# # print(courses)
# # print(courses[0])

# # insert list items into a list:
# courses.extend(courses2)
# print(courses)

# # remove item from a list:
# courses.remove('Math')
# print(courses)

# # pop item from a list:
# popped = courses.pop()
# print(popped)
# print(courses)

# # reverse a list:
# courses.reverse()
# print(courses)

# # sort a list:
# courses.sort()
# print(courses)
# nums.sort()
# print(nums)

# # sort in reverse order:
# courses.sort(reverse=True)
# print(courses)
# nums.sort(reverse=True)
# print(nums)

# sorted_courses = sorted(courses)
# print(sorted_courses)

# # find max and min , sum:
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# # find index value in list:
# print(courses.index('CompSci'))

# #find item in a list
# print('Math' in courses)
# print('Art' in courses)

# for course in courses:
#     print(course)

# for index, course in enumerate(courses):
#     print(index, course)

# for index, course in enumerate(courses, start=1):
#     print(index, course)

# # list items into string:
# course_str = '-'.join(courses)
# print(course_str)

# #split string into list:
# splited_list = course_str.split('-')
# print(splited_list)


# # Mutable:
# list_1 = ['History' , 'Math', 'Physics', 'CompSci']
# list_2 = list_1
# print(list_1)
# print(list_2)
# list_1[0] = 'Art'
# print(list_1)
# print(list_2)

# # Tuple:
# # Immutable:
# tuple_1 = ('History' , 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# tuple_1[0] = 'Art' #error for replce but other func work
# print(tuple_1)
# print(tuple_2)

# Sets:
cs_courses = {'History' , 'Math', 'Physics', 'CompSci'}
art_courses = {'History' , 'Math', 'Art', 'Design'}
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# # Summary:
# # Empty Lists:
# empty_list = []
# empty_list = list()

# # Empty tuples:
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Sets:
# empty_set = {} # Error here  
# empty_set = set()