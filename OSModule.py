import os
from datetime import datetime
import sys

# get current directory:
print(os.getcwd())

# # change directory:
# os.chdir('c:\Users\User\Desktop')

# # make directory:
# os.mkdir('example')
# os.makedirs('example/sub_exp')

# # remove directory:
# os.rmdir('example')
# os.removedirs('example/sub_exp')

# # rename:
# os.rename('current_file.txt', 'new_file.txt')

# # Look at info about files:
# os.stat(test.txt)
# Useful stat results: st_size (bytes), st_mtime (time stamp)
# mod = os.stat('Functions.py')
# mod_time = os.stat('Functions.py').st_mtime
# mod_size = os.stat('Functions.py').st_size
# print(mod)
# print(datetime.fromtimestamp(mod_time))
# print(mod_size)

# # To see entire directory tree and files within
# # os.walk is a generator that yields a tuple of 3 values as it walks the directory tree
# # This is useful for locating a file that you can’t remember where it was
# # If you had a web app, and you wanted to keep track of the file info within a certain
# #  directory structure, then you could to thru the os.walk method and go thru all files 
# # and folders and collect file information.

# os.chdir('/Users/User/Desktop/hi')
# for dirpath, dirnames, filenames in os.walk('/Users/User/Desktop/hi'): 
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

# Join path:
# os.chdir('/Users/User/Desktop/')
# print(os.environ)
print((os.environ.get('HOMEPATH')))
'''mission \ sign'''
file_path = os.environ.get('HOMEPATH') + 'test.txt'
print(file_path) 
''' slove mission \ sign '''
file_path2 = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
print(file_path2)

# This will grab filename of any path we are working on:
print(os.path.basename('/Desktop/hi/OSModule.py'))

# returns the directory:
print(os.path.dirname('/Desktop/hi/OSModule.py'))

# returns both the directory and the file as a tuple
print(os.path.split('/tmp/test.txt'))

# check path exists or not:
print(os.path.exists('/tmp/test.txt'))
print(os.path.exists('/Users/User/Desktop/hi/OSModule.py'))

# check dir and file:
print(os.path.isdir('/Users/User/Desktop/hi/OSModule.py'))
print(os.path.isdir('/Users/User/Desktop/hi/'))
print(os.path.isfile('/Users/User/Desktop/hi/OSModule.py'))

# split text:
print(os.path.splitext('/tmp/test.txt'))

# # more detail on os.function:
#print(dir(os))

# # more detail on os.path.function:
# print(dir(os.path))
