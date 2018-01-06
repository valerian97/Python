filename = 'programming.txt'

with open(filename,'a') as file_object:
	file_object.write("I love Programming!!!!!\n")
	file_object.write("Do you??\n")
with open(filename) as filereader:
	print(filereader.read())
