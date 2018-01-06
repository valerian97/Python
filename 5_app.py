import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,400,400)
		self.setWindowTitle("Window one")
		extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!",self)
		extractAction.setShortcut('Ctrl+Q')
		extractAction.setStatusTip('Leave the tip')
		extractAction.triggered.connect(self.close_application)
		self.statusBar()
		#We needto modify the menuBar so we add it to a var
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		self.home()
	
	def home(self):
		btn = QtGui.QPushButton("Quit Applicaton",self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.sizeHint())
		btn.move(100,100)
		self.show()
	
	def close_application(self):
		print("Whooaa so custom")
		sys.exit()
def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
if __name__ == "__main__":
	run()
