try:
	firstNum = input('Enter first number: ')
	secondNum = input('Enter Second number: ')
	answer = int(firstNum)/int(secondNum)
	print(answer)
except ZeroDivisionError:
	print('Error: Tried to divide by 0')
except NameError,TypeError:
	print('Error: Invalid input type')
