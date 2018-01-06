import datetime
from textSplitter import splitText
names = ['Vector Analysis', 'Electrostatics']
descriptions = ['Cartesian, cylindrical and spherical coordinate systems, - Divergence, gradient, curl, and Laplacian - Divergence and Strokes theorems.', 'Coulombs Law, Electric Field intensity - Field due to continunous line, surface, volume charges - Electric flux density - Gauss Law - Energency expended in moving a  charge in an electric field - Potential & potential graident - Electric Dipole']
startDates = [datetime.date(2017,7,14), datetime.date(2017,7,22)]
endDates = [datetime.date(2017,7,21), datetime.date(2017,8,4)]
hours = [3,5]
rows = [list(str(i+1) for i in range(len(names))), names,descriptions,str(hours),list(str(i) for i in startDates),list(str(i) for i in endDates)]
def queryData():
	pass
def dispUgly():
	for i in range(len(names)):
		print('Names: ' + names[i])
		print('Description: ' + descriptions[i])
		print('Start Date: ' + str(startDates[i]))
		print('End Date: ' + str(endDates[i]))
		print('Hour: ' + str(hours[i]))
def dispTable():
	#No Topic Hr Start Dt End Dt
	NoLength = 2
	topicLength = 25
	DescriptionLength = 60
	HoursLength = 2
	DateLength = 10
	columnLengths = [2,25,60,2,10,10]
	titles = ['No','Topic','Description','Hr','Start Dt', 'End Dt']
	print('+' + '-'*(NoLength+2) +'+' + '-'*(topicLength+2) + '+' + '-'*(DescriptionLength+2) + '+' + '-'*(HoursLength+2) + '+' + '-'*(DateLength+2) + '+' + '-'*(DateLength+2) + '+')
	for i in range(len(titles)):
		print('|'+' '+titles[i]+' '*(columnLengths[i] - len(titles[i])),end = ' ')
	print('|')
	print('+' + '-'*(NoLength+2) +'+' + '-'*(topicLength+2) + '+' + '-'*(DescriptionLength+2) + '+' + '-'*(HoursLength+2) + '+' + '-'*(DateLength+2) + '+' + '-'*(DateLength+2) + '+')
	for entryNo in range(len(names)):
		title = splitText(names[entryNo], columnLengths[1])
		description = splitText(descriptions[entryNo], columnLengths[2])
		print(title)
		print(description)
dispTable() 
