import sys
#import requests
print(sys.executable)

message = 'Hello World'

New_message = message.replace('World', 'Universe')

# problem: 'Boddy's World'
message2 = "Boddy's World"

# print it in new line form
message3 = """Boddy's World was a good
cartoon in the 10990s"""

greeting = "Hello"
name = 'wq'

# string concatenation
add_message = greeting + ', ' + name
add_message2 = '{}, {}, Welcome!'.format(greeting, name)
add_message3 = f'{greeting}, {name}, Welcome!'

print(message)
print(len(message))
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])
print(message[5:11])
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find("World"))
print(message.find("Universe"))
print(New_message)
print(add_message)
print(add_message2)
print(add_message3)

# more information
#print(dir(name))
#print(help(str))
#print(help(str.lower))
