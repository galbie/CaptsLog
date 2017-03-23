# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created: Thu Mar 09 12:32:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(400,270)
		
        self.formLayoutWidget = QtGui.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 60, 261, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
		
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
		
        self.username = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.username)
		
        self.password1 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.password1.setFont(font)
        self.password1.setObjectName("password1")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.password1)
		
        self.password2 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.password2.setFont(font)
        self.password2.setObjectName("password2")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.password2)
		
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem1)
		
        self.iusername = QtGui.QLineEdit(self.formLayoutWidget)
        self.iusername.setObjectName("iusername")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.iusername)
		
        self.ipassword1 = QtGui.QLineEdit(self.formLayoutWidget)
        self.ipassword1.setObjectName("ipassword1")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.ipassword1)
		
        self.ipassword2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.ipassword2.setObjectName("ipassword2")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.ipassword2)
		
        self.ErrorMessage = QtGui.QLabel(Form)
        self.ErrorMessage.setGeometry(QtCore.QRect(160, 190, 46, 13))
        self.ErrorMessage.setText("")
        self.ErrorMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorMessage.setObjectName("ErrorMessage")
		
        self.Descision = QtGui.QDialogButtonBox(Form)
        self.Descision.setGeometry(QtCore.QRect(220, 220, 156, 23))
        self.Descision.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.Descision.setObjectName("Descision")
		
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 321, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.username.setText(QtGui.QApplication.translate("Form", "Username :", None, QtGui.QApplication.UnicodeUTF8))
        self.password1.setText(QtGui.QApplication.translate("Form", "Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.password2.setText(QtGui.QApplication.translate("Form", "Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Please enter your Username and Password (at least 4 characters)", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

