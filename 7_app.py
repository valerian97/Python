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
        
        dispAction = QtGui.QAction("&Display msg", self)
        dispAction.setShortcut("Ctrl+D")
        dispAction.setStatusTip("Display a message")
        dispAction.triggered.connect(self.msg)
        
        runAction = QtGui.QAction("&Run", self)
        runAction.setShortcut("Ctrl+R")
        runAction.setStatusTip("This doesn't do anything really")
        runAction.triggered.connect(self.msg)
        self.statusBar()
        
        #MenuBar is assignmed to a variable because we want to modify it
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        fileMenu.addAction(dispAction)
        
        runMenu = mainMenu.addMenu("&Run")
        runMenu.addAction(runAction)
        
        self.home()
    
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.resize(btn.minimumSizeHint())
        btn.move(self.height()/2 - btn.height()/2, self.width()/2 - btn.width()/2)
        btn.clicked.connect(self.close_application)
        
        self.show()
    
    def close_application(self):
        print("Whoo so custom!!!")
        sys.exit()
        
    def msg(self):
        print('Menu Clicked')

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
run()
