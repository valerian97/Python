class chair(object):
	def __init__(self, name, legs = 4):
		self.name = name
		self.legs = legs
	def printz(self):
		print(self.name + ' ' + str(self.legs))

inst1 = chair("Ramesh")
inst1.printz()
inst2 = chair("Rocky",1)
inst2.printz()
