import sys
from PyQt4 import QtGui,QtCore

class Window(QtGui.QMainWindow):
	
	def __init__(self):
		super(Window,self).__init__()
		self.setWindowTitle('My Program')
		self.setGeometry(100,100,400,400)
		
		
		self.home()
	
	def home(self):
		btn = QtGui.QPushButton('Quit', self)
		btn.resize(btn.minimumSizeHint())
		btn.move(self.height()/2 - btn.height()/2, self.width()/2 - btn.width()/2)
		btn.clicked.connect(self.close_application)
		self.show()
	
	def close_application(self):
		print('Quitting application')
		sys.exit()

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()
