def splitText(text, length):
	#text = "All your bases are belonging to us man, haha haha haha muhahahahaha"
	#length = 20
	words = text.split(' ')
	lines = []
	word = ''
	itr = 0
	while(itr<len(words)):
		if(len(word + ' ' + words[itr])<=length):
			word = word + ' ' + words[itr]
			if(itr == len(words)-1):
				lines.append(word)
		else:
			lines.append(word)
			word = ''
			continue
		itr += 1
	#for line in lines:
	#	print(str(len(line)) + ' : ' + line)
	return lines
def extendList(inputList, length):
	outputList = []
	for i in range(length):
		if(i < len(inputList)):
			outputList.append(inputList[i])
		else:
			outputList.append('')
	return outputList
lines = splitText("ALL your chics are beloning to us, mahahahaha. Bow down now in shame and fear!", 30)
print(extendList([1,2,3,4],10))

for line in lines:
	print(str(len(line)) + ' : ' + line)
