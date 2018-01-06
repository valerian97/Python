def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
	charList = list(chars)
	result = []
	for char in text:
		if char in charList:
			result.append(char)
	return result

text = input('Enter some text: ')
chars = input('Enter some chars: ')
if(chars != ''):
	print(valid(text,chars))
else:
	print(valid(text))
