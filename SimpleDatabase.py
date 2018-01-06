people = {
	'Alice':{
		'phone':'2341',
		'addr':'Foo drive 23'
	},
	'Beth':{
		'phone':'9102',
		'addr':'Bar street 42'
	}
}
	
def update(name,phone,addr):
	global people
	people[name] = {'phone':phone,
					'addr':addr
					}
	print('Database successfully updated!')
def disp():
	for key in people.keys():
		print(key + '\n' + people[key]['phone'] +'\n' + people[key]['addr'] + '\n' + '--------')
def request(key, param):
	if(key == 'p' or key == 'P'):
		for person in people:
			if people[person]['phone'] == param:
				print(person + '\n' + people[person]['phone'] +'\n' + people[person]['addr'])
	elif(key == 'a' or key == 'A'):
		for person in people:
			if people[person]['addr'] == param:
				print(person + '\n' + people[person]['phone'] +'\n' + people[person]['addr'])
	else:
		print('Invalid Request!')
