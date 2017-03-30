# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
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


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        """Setting up Main window UI.
        """
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(550, 682)

        # Size Policy
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())

        # Main Window
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setDocumentMode(False)

        # Central Widget
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        # Horizontal Layout 7, Journal Table Layout
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_7.setMargin(11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.journalTableLayout = QtGui.QHBoxLayout()
        self.journalTableLayout.setMargin(11)
        self.journalTableLayout.setSpacing(6)
        self.journalTableLayout.setObjectName(_fromUtf8("journalTableLayout"))
        self.journalList = QtGui.QListWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Journal List
        sizePolicy.setHeightForWidth(
            self.journalList.sizePolicy().hasHeightForWidth())
        self.journalList.setSizePolicy(sizePolicy)
        self.journalList.setMinimumSize(QtCore.QSize(100, 600))
        self.journalList.setMaximumSize(QtCore.QSize(250, 16777215))
        self.journalList.setObjectName(_fromUtf8("journalList"))
        self.journalTableLayout.addWidget(self.journalList)

        # Journal Entry Layout
        self.horizontalLayout_7.addLayout(self.journalTableLayout)
        self.journalEntryLayout = QtGui.QHBoxLayout()
        self.journalEntryLayout.setMargin(11)
        self.journalEntryLayout.setSpacing(6)
        self.journalEntryLayout.setObjectName(_fromUtf8("journalEntryLayout"))
        self.journalEntry = QtGui.QPlainTextEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.journalEntry.sizePolicy().hasHeightForWidth())

        # Journal Entry
        self.journalEntry.setSizePolicy(sizePolicy)
        self.journalEntry.setMinimumSize(QtCore.QSize(200, 600))
        self.journalEntry.setObjectName(_fromUtf8("journalEntry"))
        self.journalEntryLayout.addWidget(self.journalEntry)
        self.horizontalLayout_7.addLayout(self.journalEntryLayout)

        # Journal View Layout
        self.journalViewLayout = QtGui.QHBoxLayout()
        self.journalViewLayout.setMargin(11)
        self.journalViewLayout.setSpacing(6)
        self.journalViewLayout.setObjectName(_fromUtf8("journalViewLayout"))

        # Journal View
        self.journalView = QtGui.QTextEdit(self.centralWidget)
        self.journalView.setMinimumSize(QtCore.QSize(200, 600))
        self.journalView.setObjectName(_fromUtf8("journalView"))
        self.journalViewLayout.addWidget(self.journalView)
        self.horizontalLayout_7.addLayout(self.journalViewLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        # Menu Bar
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 550, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew_Entry = QtGui.QAction(MainWindow)
        self.actionNew_Entry.setObjectName(_fromUtf8("actionNew_Entry"))
        self.menuFile.addAction(self.actionNew_Entry)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Captslog", "Captslog", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionNew_Entry.setText(
            _translate("MainWindow", "New Entry", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
