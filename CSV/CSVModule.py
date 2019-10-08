import csv
import os
os.chdir('/Users/User/Desktop/hi/CSV')

# # Read CSV file:
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for line in csv_reader:
#         print(line[2])

# # Write new CSV file:
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')

#         for line in csv_reader:
#             #print(line)
#             csv_writer.writerow(line)

# # Write new CSV file2:
# if you have new csv file with blank lines  this is for you
# # Python 2:
# with open('new_names.csv', 'wb') as outfile:
#     writer = csv.writer(outfile)
# # Python 3:
# with open('new_names.csv', 'w', newline='') as outfile:
#     writer = csv.writer(outfile)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            print(line)
            csv_writer.writerow(line)