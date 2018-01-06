import os
names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
	print('Hello there, ' + name)
print('Second Method: ')

for name in names:
	print(' '.join(['Hello There', name]))

print('Third Method:')
#Concatinating multiple strings, we should use this
print(', '.join(names))

location_of_files = '/home/carlton/Documents/Programming/Python'
file_name = 'Test.txt'
print('/'.join([location_of_files,file_name]))

with open(os.path.join(location_of_files, file_name)) as f:
	print(f.read())
#String Formatting
who = 'Gary'
how_many = 12

# <Name> bought <Num> apples today!
print(who,' bought ', how_many, ' apples today!')
print('{0} bought {1} apples today!'.format(who,how_many))
