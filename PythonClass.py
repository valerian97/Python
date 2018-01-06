__metaclass__ = type
class Person:
	def setName(self, name):
		self.name = name
	def getName(self):
		return self.name
	def greet(self):
		print("Hello, World! I'm " + self.name)
foo = Person()
bar = Person()
foo.setName("Luke SkyWalker")
bar.setName("Anakin SkyWalker")
foo.greet()
bar.greet()
