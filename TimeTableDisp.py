slotList = {'A1':'ECE2003', 'B1':'ECE2002','C1':'ECE1003','D1':'CSE2004','E1':'STS2001','F1':'MAT2002','G1':'ECE1004',
            'TF1':'MAT2002','TE1':'STS2001','TD1':'ECE1005', 'L31':'CSE2004','L32':'CSE2004','L45':'ECE2002','L46':'ECE2002',
            'L51':'ECE2001','L52':'ECE2001','L55':'MAT2002','L56':'MAT2002'}
days = ['Mon', 'Tue','Wed','Thu','Fri']
TimeTable = {'Mon':[('A1','L1'),('F1','L2'),('D1','L3'),('TB1','L4'),('TG1','L5'),('N','L6'),'L',('A2','L31'),('F2','L32'),('D2','L33'),('TB2','L34'),('TG2','L35'),('N','L36')],
			 'Tue':[('B1','L7'),('G1','L8'),('E1','L9'),('TC1','L10'),('TAA1','L11'),('N','L12'),'L',('B2','L37'),('G2','L38'),('E2','L39'),('TC2','L40'),('TAA2','L41'),('N','L42')],
			 'Wed':[('C1','L13'),('A1','L14'),('F1','L15'),('N','L16'),('N','L17'),('N','L18'),'L',('C2','L43'),('A2','L44'),('F2','L45'),('TD2','L46'),('TBB2','L47'),('N','L48')],
			 'Thu':[('D1','L19'),('B1','L20'),('G1','L21'),('TE1','L22'),('TCC1','L23'),('N','L24'),'L',('D2','L49'),('B2','L50'),('G2','L51'),('TE2','L52'),('TCC2','L53'),('N','L54')],
			 'Fri':[('E1','L25'),('C1','L26'),('TA1','L27'),('TF1','L28'),('TD1','L29'),('N','L30'),'L',('E2','L55'),('C2','L56'),('TA2','L57'),('TF2','L58'),('TDD2','L59'),('N','L60')]}
cellLength = 9;
def dispTable():
	print('')
	print('', end='+')
	for i in range(13):
		print('-'*cellLength, end = '+')
	print()
	for day in days:
		for slot in TimeTable[day]:
			if slot[0] in slotList.keys():
				print('|' + ' ' + slotList[slot[0]], end = ' ')
			elif slot == 'L':
				print('|' + '  ' + 'Lunch' + '  ', end ='')
			elif slot[1] in slotList.keys():
				print('|' + ' ' + slotList[slot[1]], end = ' ')
			else:
				print('|' + ' '*8, end = ' ')
		print('|')
		for slot in TimeTable[day]:
			if slot[0] in slotList.keys():
				print('|' + ' '*3 + slot[0] + ' '*(6-len(slot[0])),end = '')
			elif slot == 'L':
				print('|' + '  ' + '     ' + '  ', end ='')
			elif slot[1] in slotList.keys():
				print('|' + ' '*3 + slot[1] + ' '*(6-len(slot[1])),end = '')
			else:
				print('|' + ' '*8, end = ' ')
		print('|') 
		print('', end='+')
		for i in range(13):
			print('-'*cellLength,end ='+')
		print()
def dispGui():
	pass
def updateSlots(slot, subject):
	slotList[slot] = subject
def delSlot(slot):
	del slotList[slot]
def querySlots():
	pass
def commitSlots():
	pass
dispTable()
