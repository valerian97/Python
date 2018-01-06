import sys
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Hello World")
window.setGeometry(50,50,400,400)
window.show()
sys.exit(app.exec_())
