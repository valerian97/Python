try:
	x = input('Enter the first number: ')
	y = input('Enter the second number: ')
	print (int(x)/int(y))
except(ZeroDivisionError,TypeError,ValueError), e:
	print(e)
