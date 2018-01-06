import sys 
from PyQt4 import QtGui,QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        
        super(Window,self).__init__()
        self.setWindowTitle("My program")
        self.setGeometry(100,100,400,400)
        
        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)
        
        self.statusBar()
        
        #MenuBar is assignmed to a variable because we want to modify it
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        
        self.home()
    
    def home(self):
		
		btn = QtGui.QPushButton("Quit", self)
		btn.resize(btn.minimumSizeHint())
		btn.move(self.height()/2 - btn.height()/2, self.width()/2 - btn.width()/2)
		btn.clicked.connect(self.close_application)
		extractAction = QtGui.QAction(QtGui.QIcon('iconn.png'),'Flee the Scene',self)
		extractAction.triggered.connect(self.close_application)
		
		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(200,200)
		checkBox.stateChanged.connect(self.enlarge_window)
		checkBox.toggle()
		
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200,80,250,20)
		
		self.btn = QtGui.QPushButton("Download", self)
		self.btn.move(200,120)
		self.btn.clicked.connect(self.download)
		
		print(self.style().objectName())
		self.styleChoice = QtGui.QLabel("Linux",self)
		
		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("cde")
		comboBox.addItem('Plastique')
		comboBox.addItem('Cleanlooks')
		
		comboBox.move(50,250)
		self.styleChoice.move(50,150)
		comboBox.activated[str].connect(self.style_choice)
		
		self.toolbar = self.addToolBar("Extraction")
		self.toolbar.addAction(extractAction)
		
		fontChoice = QtGui.QAction('Font',self)
		fontChoice.triggered.connect(self.font_choice)
		self.toolbar = self.addToolBar('Font Choice')
		self.toolbar.addAction(fontChoice)
		
		color= QtGui.QColor(0,0,0)
		
		fontColor = QtGui.QAction('Font bg Color', self)
		fontColor.triggered.connect(self.color_picker)
		
		self.toolbar.addAction(fontColor)
		
		cal = QtGui.QCalendarWidget(self)
		cal.move(500,200)
		cal.resize(200,200)
		
		self.show()
    
    def color_picker(self):
		color = QtGui.QColorDialog.getColor()
		
		self.styleChoice.setStyleSheet("QWidget { background-color: %s}" %color.name())
    def font_choice(self):
		font,valid = QtGui.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)
		
    def style_choice(self,text):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
    
    def enlarge_window(self,state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,1000,600)
		else:
			self.setGeometry(50,50,500,300)
    
    def download(self):
		self.completed = 0
		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)
    def close_application(self):
        
		choice = QtGui.QMessageBox.question(self, 'Extract!', 'Get into the chopper?',QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
		if(choice == QtGui.QMessageBox.Yes):
			print('Extracting now!!!')
			sys.exit()
		
        
    def msg(self):
        print('Menu Clicked')

def run():
    
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
run()
