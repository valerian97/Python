def describePerson(person):
	print('Description of ' + person['name'])
	print('Age : ' + person['age'])
	try: print('Occupation: ', person['occupation'])
	except KeyError: pass
describePerson({'age':'12','name':'Ravikanth', 'occupation':'Sadist'})
describePerson({'age':'14','name':'Carlton'})
