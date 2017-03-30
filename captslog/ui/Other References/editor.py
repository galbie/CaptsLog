# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainp.ui'
#
# Created: Mon Mar 13 12:55:15 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide import QtWebKit


class UI_MainWindow(object):

    def setupUi(self, MainWindow):
        """Setting up UI for Main Window
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 600)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.txtInput = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtInput.setObjectName("MarkDtextEdit")
        self.horizontalLayout.addWidget(self.txtInput)

        self.txtOutput = QtGui.QTextEdit(self.centralwidget)
        self.txtOutput.setObjectName("MarkDownView")
        self.horizontalLayout.addWidget(self.txtOutput)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
