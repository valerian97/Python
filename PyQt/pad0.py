# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pad.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from functools import partial
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 294)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.result = QtGui.QLineEdit(Form)
        self.result.setReadOnly(True)
        self.result.setObjectName(_fromUtf8("result"))
        self.verticalLayout.addWidget(self.result)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.seven = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy)
        self.seven.setObjectName(_fromUtf8("seven"))
        self.gridLayout.addWidget(self.seven, 2, 0, 1, 1)
        self.eight = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy)
        self.eight.setObjectName(_fromUtf8("eight"))
        self.gridLayout.addWidget(self.eight, 2, 1, 1, 1)
        self.three = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy)
        self.three.setObjectName(_fromUtf8("three"))
        self.gridLayout.addWidget(self.three, 0, 2, 1, 1)
        self.subtract = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtract.sizePolicy().hasHeightForWidth())
        self.subtract.setSizePolicy(sizePolicy)
        self.subtract.setObjectName(_fromUtf8("subtract"))
        self.gridLayout.addWidget(self.subtract, 3, 2, 1, 1)
        self.one = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setObjectName(_fromUtf8("one"))
        self.gridLayout.addWidget(self.one, 0, 0, 1, 1)
        self.four = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four.sizePolicy().hasHeightForWidth())
        self.four.setSizePolicy(sizePolicy)
        self.four.setObjectName(_fromUtf8("four"))
        self.gridLayout.addWidget(self.four, 1, 0, 1, 1)
        self.equalTo = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalTo.sizePolicy().hasHeightForWidth())
        self.equalTo.setSizePolicy(sizePolicy)
        self.equalTo.setObjectName(_fromUtf8("equalTo"))
        self.gridLayout.addWidget(self.equalTo, 3, 1, 1, 1)
        self.nine = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy)
        self.nine.setObjectName(_fromUtf8("nine"))
        self.gridLayout.addWidget(self.nine, 2, 2, 1, 1)
        self.six = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy)
        self.six.setObjectName(_fromUtf8("six"))
        self.gridLayout.addWidget(self.six, 1, 2, 1, 1)
        self.add = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setObjectName(_fromUtf8("add"))
        self.gridLayout.addWidget(self.add, 3, 0, 1, 1)
        self.two = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy)
        self.two.setObjectName(_fromUtf8("two"))
        self.gridLayout.addWidget(self.two, 0, 1, 1, 1)
        self.five = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy)
        self.five.setObjectName(_fromUtf8("five"))
        self.gridLayout.addWidget(self.five, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.setup_events()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.seven.setText(_translate("Form", "7", None))
        self.seven.setShortcut(_translate("Form", "7", None))
        self.eight.setText(_translate("Form", "8", None))
        self.eight.setShortcut(_translate("Form", "8", None))
        self.three.setText(_translate("Form", "3", None))
        self.three.setShortcut(_translate("Form", "3", None))
        self.subtract.setText(_translate("Form", "-", None))
        self.subtract.setShortcut(_translate("Form", "-", None))
        self.one.setText(_translate("Form", "1", None))
        self.one.setShortcut(_translate("Form", "1", None))
        self.four.setText(_translate("Form", "4", None))
        self.four.setShortcut(_translate("Form", "4", None))
        self.equalTo.setText(_translate("Form", "=", None))
        self.equalTo.setShortcut(_translate("Form", "Return", None))
        self.nine.setText(_translate("Form", "9", None))
        self.nine.setShortcut(_translate("Form", "9", None))
        self.six.setText(_translate("Form", "6", None))
        self.six.setShortcut(_translate("Form", "6", None))
        self.add.setText(_translate("Form", "+", None))
        self.add.setShortcut(_translate("Form", "+", None))
        self.two.setText(_translate("Form", "2", None))
        self.two.setShortcut(_translate("Form", "2", None))
        self.five.setText(_translate("Form", "5", None))
        self.five.setShortcut(_translate("Form", "5", None))

    def setup_events(self):
        self.one.clicked.connect(partial(self.handler,arg = "1"))
        self.two.clicked.connect(partial(self.handler,arg = '2'))
        self.three.clicked.connect(partial(self.handler,arg = '3'))
        self.four.clicked.connect(partial(self.handler,arg = '4'))
        self.five.clicked.connect(partial(self.handler,arg = '5'))
        self.six.clicked.connect(partial(self.handler,arg = '6'))
        self.seven.clicked.connect(partial(self.handler,arg = '7'))
        self.eight.clicked.connect(partial(self.handler,arg = '8'))
        self.nine.clicked.connect(partial(self.handler,arg = '9'))
        self.equalTo.clicked.connect(partial(self.handler,arg = '='))
        self.add.clicked.connect(partial(self.handler,arg = '+'))
        self.subtract.clicked.connect(partial(self.handler,arg = '-'))
    
    def handler(self,arg):
        if(arg == '='):
            words = self.result.text()
            ans = eval(str(words))
            self.result.setText(str(ans))
 if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
