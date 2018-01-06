import sys
from PyQt4 import QtGui,QtCore
#QtCore for eventhandling
class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,400,300)
		self.setWindowTitle("My First Window")
		self.home()
	#Specific to page
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(100,100)
		btn.move(100,100)
		self.show()
def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
run()
