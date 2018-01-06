try:
	x = input('Enter the first number: ')
	y = input('Enter the second number: ')
	print(str(int(x)/int(y)))
except ZeroDivisionError:
	print('The second number cannot be zero!')
except ValueError:
	print('That wasnt a number, was it?')
