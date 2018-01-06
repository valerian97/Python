import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setWindowTitle('My App')
		self.setGeometry(50,50,400,400)
		
		extractAction = QtGui.QAction("&Exit",self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip("Exit the app")
		extractAction.triggered.connect(self.quitApp)
		
		self.statusBar()
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("&File")
		fileMenu.addAction(extractAction)
		
		self.home()
		
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.resize(btn.sizeHint())
		btn.move(200,200)
		btn.clicked.connect(self.quitApp)
		
		extractAction = QtGui.QAction(QtGui.QIcon('iconn.png'),'Flee the scene', self)
		extractAction.triggered.connect(self.quitApp)
		
		checkBox = QtGui.QCheckBox('Enlarge Window',self)
		checkBox.toggle()
		checkBox.move(150,150)
		checkBox.stateChanged.connect(self.enlargeWindow)
		
		self.toolBar = self.addToolBar("Extraction")
		self.toolBar.addAction(extractAction)
		
		self.show()
	
	def enlargeWindow(self,state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,700,700)
		else:
			self.setGeometry(50,50,400,400)
	def quitApp(self):
		choice = QtGui.QMessageBox.question(self,'Extract!','Get into the chopper?', QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print('So cool')
			sys.exit()

def run():
	app =QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	run()
