import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,400,400)
		self.setWindowTitle("Window one")
		self.home()
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(70,30)
		btn.move(100,100)
		self.show()
def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
if __name__ == "__main__":
	run()

