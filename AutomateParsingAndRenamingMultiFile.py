import os 

os.chdir('/Users/User/Desktop/hi/example_material - Copy')

# print(os.getcwd())

# # 1:
# for f in os.listdir():
#     # print(f)
#     f_name, f_ext = (os.path.splitext(f))
#     # print(f_name.split('-'))
#     f_title, f_course, f_num = f_name.split('-')
#     # print(f_title)
#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     f_num = f_num.strip()[1:]
#     print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

    
# 2:
for f in os.listdir():
    # print(f)
    f_name, f_ext = (os.path.splitext(f))
    # print(f_name.split('-'))
    
    # recommented by comment:
    f_title, f_course, f_num = f_name.split(' - ')
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

# # 3:
# for f in os.listdir():
#     f_name, f_ext = (os.path.splitext(f))
#     f_title, f_course, f_num = f_name.split('-')
#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     f_num = f_num.strip()[1:].zfill(2)
#     # print('{}-{}{}'.format(f_num, f_title, f_ext))
#     new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
#     os.rename(f, new_name)

