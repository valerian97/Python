# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TempCoverter.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(372, 241)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.fLineEdit = QtGui.QLineEdit(Form)
        self.fLineEdit.setObjectName(_fromUtf8("fLineEdit"))
        self.horizontalLayout.addWidget(self.fLineEdit)
        self.fButton = QtGui.QPushButton(Form)
        self.fButton.setObjectName(_fromUtf8("fButton"))
        self.horizontalLayout.addWidget(self.fButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cLineEdit = QtGui.QLineEdit(Form)
        self.cLineEdit.setObjectName(_fromUtf8("cLineEdit"))
        self.horizontalLayout_2.addWidget(self.cLineEdit)
        self.cButton = QtGui.QPushButton(Form)
        self.cButton.setObjectName(_fromUtf8("cButton"))
        self.horizontalLayout_2.addWidget(self.cButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.kLineEdit = QtGui.QLineEdit(Form)
        self.kLineEdit.setObjectName(_fromUtf8("kLineEdit"))
        self.horizontalLayout_3.addWidget(self.kLineEdit)
        self.kButton = QtGui.QPushButton(Form)
        self.kButton.setObjectName(_fromUtf8("kButton"))
        self.horizontalLayout_3.addWidget(self.kButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.exitButton = QtGui.QPushButton(Form)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.verticalLayout.addWidget(self.exitButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_4.setText(_translate("Form", "Temperature Converter", None))
        self.label.setText(_translate("Form", "Farenheit", None))
        self.fButton.setText(_translate("Form", "Go", None))
        self.label_2.setText(_translate("Form", "Celcius", None))
        self.cButton.setText(_translate("Form", "Go", None))
        self.label_3.setText(_translate("Form", "Kelvin", None))
        self.kButton.setText(_translate("Form", "Go", None))
        self.exitButton.setText(_translate("Form", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

