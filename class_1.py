class Person:
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name
	def greet(self):
		print('Hello there, ' + self.name)
foo = Person()
doo = Person()
foo.setName("Ramesh")
doo.setName('Rajesh')
foo.greet()
doo.greet()
