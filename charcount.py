def charcount(text):
	dicts = {}
	for char in text:
		if char in dicts.keys():
			dicts[char] += 1
		else:
			dicts[char] = 1
	return dicts
text = input('Enter some text: ')
print(charcount(text))
