import sys
from PyQt4 import QtGui
#sys.argv: command line can pass arguments to that
app = QtGui.QApplication([])
window = QtGui.QWidget()
window.setGeometry(50,50,300,250)
window.setWindowTitle("This is the window!")
window.show()
sys.exit(app.exec_())
