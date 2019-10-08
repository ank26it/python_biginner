# Comparisons:
# Equal:          ==
# Not Equal:      !=
# Greater Than:   >
# Less Than:      <
# GreaterOrEqual: >=
# LessOrEqual:    <=
# Object Identity:is
# and 
# or
# not

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', () , []
# Any empty mapping. For example, {}


language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'C':
    print(' Language is C')
else:
    print("No Match")

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print('id of a: ' + str(id(a)))
print(id(b))
print(id(c))
print(a is b)
print(a is c)
print(id(a) == id(c))

# Test False Values:
condition = []
if condition:
    print('Evaluted to TRUE')
else:
    print('Evalutes to FALSE')
