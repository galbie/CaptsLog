# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Thu Mar 09 12:32:10 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(400, 300)
		
        self.formLayoutWidget = QtGui.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 110, 251, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
		
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
		
        self.Username = QtGui.QLabel(self.formLayoutWidget)
        self.Username.setObjectName("Username")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.Username)
		
        self.Password = QtGui.QLabel(self.formLayoutWidget)
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.Password)
		
        self.iUsername = QtGui.QLineEdit(self.formLayoutWidget)
        self.iUsername.setObjectName("iUsername")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.iUsername)
		
        self.iPassword = QtGui.QLineEdit(self.formLayoutWidget)
        self.iPassword.setObjectName("iPassword")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.iPassword)
		
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
		
        self.Login = QtGui.QPushButton(Form)
        self.Login.setGeometry(QtCore.QRect(210, 220, 75, 23))
        self.Login.setObjectName("Login")
		
        self.Captslog = QtGui.QLabel(Form)
        self.Captslog.setGeometry(QtCore.QRect(90, 50, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setWeight(75)
        font.setBold(True)
        self.Captslog.setFont(font)
        self.Captslog.setObjectName("Captslog")
		
        self.ErrorMessage = QtGui.QLabel(Form)
        self.ErrorMessage.setGeometry(QtCore.QRect(120, 190, 151, 20))
        self.ErrorMessage.setText("")
        self.ErrorMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorMessage.setObjectName("ErrorMessage")
		
        self.Signup = QtGui.QPushButton(Form)
        self.Signup.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.Signup.setObjectName("Signup")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.Username.setText(QtGui.QApplication.translate("Form", "Username :", None, QtGui.QApplication.UnicodeUTF8))
        self.Password.setText(QtGui.QApplication.translate("Form", "Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.Login.setText(QtGui.QApplication.translate("Form", "Log in", None, QtGui.QApplication.UnicodeUTF8))
        self.Captslog.setText(QtGui.QApplication.translate("Form", "CAPTSLOG", None, QtGui.QApplication.UnicodeUTF8))
        self.Signup.setText(QtGui.QApplication.translate("Form", "Sign Up", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

