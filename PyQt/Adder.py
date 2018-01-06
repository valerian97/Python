# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Adder.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.setup_events()
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(241, 170)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.outLineEdit = QtGui.QLineEdit(Form)
        self.outLineEdit.setReadOnly(True)
        self.outLineEdit.setObjectName(_fromUtf8("outLineEdit"))
        self.horizontalLayout_3.addWidget(self.outLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.oneLineEdit = QtGui.QLineEdit(Form)
        self.oneLineEdit.setObjectName(_fromUtf8("oneLineEdit"))
        self.horizontalLayout.addWidget(self.oneLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.twoLineEdit_2 = QtGui.QLineEdit(Form)
        self.twoLineEdit_2.setObjectName(_fromUtf8("twoLineEdit_2"))
        self.horizontalLayout_2.addWidget(self.twoLineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.addButton = QtGui.QPushButton(Form)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.verticalLayout.addWidget(self.addButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.setup_events()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_3.setText(_translate("Form", "Output", None))
        self.label.setText(_translate("Form", "Num 1", None))
        self.label_2.setText(_translate("Form", "Num 2", None))
        self.addButton.setText(_translate("Form", "Add", None))
    def setup_events(self):
        self.addButton.clicked.connect(self.prt)
        
    def prt(self):
        num1 = self.oneLineEdit.text()
        num2 = self.twoLineEdit_2.text()
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            self.outLineEdit.setText(str(num1+num2))
        except:
            QtGui.QMessageBox.information(self, "Error", "Please enter a valid number", QtGui.QMessageBox.Ok)
        
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

