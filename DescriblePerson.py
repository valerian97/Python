def describePerson(person):
	print('Description of ' + person['name'])
	print('Age : ' + person['age'])
	if 'occupation' in person:
		print('Occupation: ' + person['occupation'])
describePerson({'age':'12','name':'Ravikanth', 'occupation':'Sadist'})
describePerson({'age':'14','name':'Carlton'})
