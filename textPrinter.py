text = ""
textWidth = 1
textLength = 0
leftMargin = 0
textHeigth = 0
lines = []
def initialize(txt,width,margin):
	global text 
	text=txt
	global textWidth
	textWidth = width
	global leftMargin
	leftMargin = margin
	global textLength 
	textLength = len(text)
def calcParameters():
	global lines
	lines = [text[i:i+textWidth] for i in range(0,textLength,textWidth)]
	textHeight = len(lines)
def display():
	print(' '*leftMargin +'+' + '-'*(4+textWidth) + '+')
	print(' '*leftMargin +'|' + ' '*(4+textWidth) +'|')
	for line in lines:
		print(' '*leftMargin +'|'+' '*(2) + line + ' '*(2 + (textWidth-len(line))) +'|')
	print(' '*leftMargin +'|' + ' '*(4+textWidth) +'|')
	print(' '*leftMargin +'+' + '-'*(4+textWidth) + '+')
	
